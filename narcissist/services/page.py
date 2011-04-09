# -*- coding: utf-8 -*-

"""
narcissist.services.page
------------------------

Definition of the Page service.

"""

from .service import Service
from jinja2 import FileSystemLoader, Environment
from ..main import app
import os

class Page(Service):
    """ Page Service - renders a jinja2 template from a file. """

    def __init__(self, extra):
        
        self.file_name = extra.get("file")
        self.extra = extra

        # set up the template loader
        loader = FileSystemLoader(app.root_path)
        env = Environment(loader = loader)
        self.template = env.get_template(self.file_name)

    def render(self):
        #render the template and pass it back
        return self.template.render(**self.extra.get("context", {}))
