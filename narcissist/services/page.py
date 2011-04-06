from .service import Service
from jinja2 import FileSystemLoader, Environment
from ..main import app
import os

class Page(Service):

    def __init__(self, extra):
        self.file_name = extra.get("file")
        self.extra = extra

        loader = FileSystemLoader(app.root_path)
        env = Environment(loader = loader)
        self.template = env.get_template(self.file_name)

    def render(self):
        return self.template.render(**self.extra.get("context", {}))
