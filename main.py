from flask import Flask, render_template, request
import settings
from services import Service
from exceptions import TypeError
import os

app = Flask(__name__)

settings.ROOT_PATH = app.root_path
settings.URLS = []
settings.THEME_PATH = os.path.join(settings.ROOT_PATH, "templates", settings.THEME)



class CallableEndPoint(object):

    def __init__(self, service):
        self.service = service

    def __call__(self):
        if request.is_xhr:
            return self.service.render()
        else:
            return render_template(settings.THEME + "/main.html", 
                    content = self.service.render(), title = settings.TITLE, 
                    sub_title = settings.SUB_TITLE, urls = settings.URLS)

for service_type, name, title, extra in settings.SERVICES:
    try:
        extra["main_settings"] = settings
        service = Service.load(service_type, extra)
        ep = CallableEndPoint(service)
        
        if service_type == name:
            url_rule = "/%s" % service_type
        else:
            url_rule = "/%s/%s" % (service_type, name,)

        if name == "index":
            url_rule = "/"

        app.add_url_rule(url_rule, name, ep)
        settings.URLS.append({"url": url_rule, "title": title})
    except TypeError, e:
        pass


if __name__ == "__main__":
    app.run(debug = True)
