from narcissist.services import Service
import settings, os
from jinja2 import Environment, FileSystemLoader
import urllib2, json

GITHUB_PATH = "https://github.com/"
GITHUB_API_PATH = GITHUB_PATH + "api/v2/json/"
GITHUB_REPOS_API_PATH = GITHUB_API_PATH + "repos/show/"

class Github(Service):

    def __init__(self, extra):
        self.extra = extra
        self.username = self.extra.get("username")

        template_path = extra.get("template_path", os.path.join(settings.ROOT_PATH, "templates"))		
        
        # Setting up the Jinja2 loader        
        env = Environment(loader = FileSystemLoader(template_path))
        self.template = env.get_template("github.html")

    def render(self):
        return self.get_repos()

    def get_repos(self):
        response = urllib2.urlopen(GITHUB_REPOS_API_PATH + self.username).read()
        return json.dumps(response)

