from .service import Service
from ..main import app
from jinja2 import Environment, FileSystemLoader
import os



class Twitter(Service):

    def __init__(self, extra):
        self.username = extra.get("username")
        self.extra = extra

        theme_path = os.path.join(app.root_path, "templates", app.config["THEME"])
        

        env = Environment(loader = FileSystemLoader(theme_path))
        self.template = env.get_template("twitter.html")

    def render(self):
        return self.template.render(username = self.username,
            **self.extra.get("context", {}))
