from flask import Flask, render_template, request
import settings
from .utils import curry
from .services import Service
from exceptions import ImportError 
import os


app = Flask(__name__)
app.root_path = os.getcwd()
settings.URLS = []


def endpoint(service):
    if request.is_xhr:
        return self.service.render()
    else:
        return render_template(settings.THEME + "/main.html", 
                content = service.render(), title = settings.TITLE, 
                sub_title = settings.SUB_TITLE, urls = settings.URLS)

def bootstrap_routes():

    for service_module, plugin, name, title, extra in settings.SERVICES:
        try:
            __import__(service_module)
            service = Service.load(plugin, extra)
            ep = curry(endpoint, service)
            
            if plugin == name:
                url_rule = "/%s" % plugin
            else:
                url_rule = "/%s/%s" % (plugin, name,)

            if name == "index":
                url_rule = "/"

            app.add_url_rule(url_rule, name, ep)
            settings.URLS.append({"url": url_rule, "title": title})
        except ImportError, e:
            pass

bootstrap_routes() 
