from .service import Service
from jinja2 import Template
import os

class Page(Service):

    def __init__(self, settings):
        self.settings = settings
        main_settings = settings.get("main_settings")
        self.template = os.path.join(main_settings.ROOT_PATH, "pages", settings.get("file", None))
    
    def render(self):
        with open(self.template) as f:
            template = Template(f.read())
            return template.render(self.settings.get("context", {}))
