from narcissist.utils import service
import os

# Your name here
TITLE = "Jovanka Gulic"

# Something about you here
SUB_TITLE = "Eve mene"

# Choose theme. ATM we have only one so deal with it.
THEME = "simple-theme"

# This is the most important part of narcissist
# We define services here. 
SERVICES = (
            # The page service with name "index" will always be rendered at /
            # The page service requires a "file" to be rendered. "file" is
            # Jinja2 template.
            service("narcissist.services.page", name = "index", title = "Bio", 
                extra = {"file": "templates/index.html"}),
            
            # The twitter service will show a timeline of your recent tweets.
            # Requires "username" in extra params
            # Uncomment next line to enable twitter service and insert your
            # username
            
            service("narcissist.services.twitter", name = "twitter", title = "@twitter", 
               extra = {"username": "twitter"},),
            
            # This only showcases how you can load your own plugins here.
            # This service will show under the url /github. If the name differs,
            # the url is /github/name.
            
            service("plugins.github", name="github", title = "My Github", extra = {"username": "jgulic"}),
            )

# Don't touch this if you don't know what are you doing.
ROOT_PATH = os.path.dirname( os.path.realpath( __file__ ) )

# This triggers debug mode. Change to False for production deployment
DEBUG = True