from narcissist.utils import service
import os

# Your name here
TITLE = "Your Name"

# Something about you here
SUB_TITLE = "YAY! I am using narcissist"

# Choose theme. ATM we have only one so deal with it.
THEME = "simple"

# This is the most important part of narcissist
# We define services here. 
SERVICES = (
            # The page service with name "index" will always be rendered at /
            # The page service requires a "file" to be rendered. "file" is
            # Jinja2 template.
            service("narcissist.services.page", name = "index", title = "Bio", 
                extra = {"file": "pages/index.html"}),
            
            # The twitter service will show a timeline of your recent tweets.
            # Requires "username" in extra params
            service("narcissist.services.twitter", name = "username", title = "@username", 
                extra = {"username": "username"},),
            
            # This only showcases how you can load your own plugins here.
            # This service will show under the url /github. If the name differs,
            # the url is /github/name.
            service("github", name="github", title = "My Github"),
            )

# Don't touch this if you don't know what are you doing.
ROOT_PATH = os.path.dirname( os.path.realpath( __file__ ) )
