from .service import Service
from jinja2 import Environment, FileSystemLoader
import os

class Twitter(Service):

    def __init__(self, settings):
        self.username = settings.get("username")
        self.settings = settings
        main_settings = settings.get("main_settings")
        env = Environment(loader = FileSystemLoader(main_settings.THEME_PATH))
        self.template = env.get_template("twitter.html")

    def render(self):
        return self.template.render(username = self.username,
                **self.settings.get("context", {}))
