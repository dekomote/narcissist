from flask import Flask, render_template, request
from .utils import curry
from .services import Service
from exceptions import ImportError 
import os, sys


app = Flask(__name__)
app.config.from_envvar('NARCISSIST_SETTINGS')
app.root_path = app.config["ROOT_PATH"]
app.config["URLS"] = []


def _endpoint(service):
    if request.is_xhr:
        return self.service.render()
    else:
        return render_template(app.config["THEME"] + "/main.html", 
                content = service.render(), title = app.config["TITLE"], 
                sub_title = app.config["SUB_TITLE"], urls = app.config["URLS"])


for service_module, plugin, name, title, extra in app.config["SERVICES"]:
    try:
        __import__(service_module)
        service = Service.load(plugin, extra)
        ep = curry(_endpoint, service)
        
        if plugin == name:
            url_rule = "/%s" % plugin
        else:
            url_rule = "/%s/%s" % (plugin, name,)

        if name == "index":
            url_rule = "/"

        app.add_url_rule(url_rule, name, ep)
        app.config["URLS"].append({"url": url_rule, "title": title})
    except ImportError, e:
        pass
