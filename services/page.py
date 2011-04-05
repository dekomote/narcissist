from .service import Service
from jinja2 import FileSystemLoader, Environment
import os

class Page(Service):

    def __init__(self, settings):
        self.file_name = settings.get("file")
        self.settings = settings
        main_settings = settings.get("main_settings")

        loader = FileSystemLoader(os.path.join(main_settings.ROOT_PATH, "pages"))
        env = Environment(loader = loader)
        self.template = env.get_template(self.file_name)

    def render(self):
        return self.template.render(**self.settings.get("context", {}))
