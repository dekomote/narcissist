# -*- coding: utf-8 -*

"""

narcissist.main
---------------

Application bootstrapping, config and routes.

"""

from flask import Flask, render_template, request
from jinja2 import FileSystemLoader
from .utils import curry
from .services import Service
from exceptions import ImportError 
import os, sys


# Setup the app and load the settings
app = Flask(__name__)
app.config.from_envvar('NARCISSIST_SETTINGS')
app.root_path = app.config["ROOT_PATH"]

main_template_path = os.path.join(app.root_path, "themes")
app.jinja_loader = FileSystemLoader(main_template_path)

# We will hold the mapped URLS in config so we can access them in the templates
app.config["URLS"] = []


def _endpoint(service):
    """ Helper for XHR requests. If the request is XHR, omit the layout. """

    if request.is_xhr:
        return self.service.render()
    else:
        return render_template(app.config["THEME"] + "/main.html", 
                content = service.render(), title = app.config["TITLE"], 
                sub_title = app.config["SUB_TITLE"], urls = app.config["URLS"])

# The routes are mapped here. The SERVICES in settings is parsed, and according
# to the entry, an url is formed and routed to the service.
for service_module, plugin, name, title, extra in app.config["SERVICES"]:
    try:
        # We need to load the service module so we can have autoload (plugins)
        __import__(service_module)

        # Factory - based on plugin name, returns an instance of a service.
        service = Service.load(plugin, extra)

        # Curry the service view function so it can also serve XHR requests
        ep = curry(_endpoint, service)
        
        # Magic
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
