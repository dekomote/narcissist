# -*- coding: utf-8 -*-

"""

narcissist.services.twitter
---------------------------

Defines Twitter Service

"""

from .service import Service
from ..main import app
from jinja2 import Environment, FileSystemLoader
import os



class Twitter(Service):

    def __init__(self, extra):

        # We need a twitter username - we can pass it in extra dict
        self.username = extra.get("username")
        self.extra = extra
        
        # We also need a template - We can get the root path and the theme from
        # the config.
        theme_path = os.path.join(app.root_path, "templates", app.config["THEME"])
        
        # Setting up the Jinja2 loader
        env = Environment(loader = FileSystemLoader(theme_path))
        self.template = env.get_template("twitter.html")

    def render(self):

        # returns the rendered template
        return self.template.render(username = self.username,
            **self.extra.get("context", {}))
