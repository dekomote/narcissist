from narcissist.services import Service

class Github(Service):
    
    def __init__(self, extra):
        self.extra = extra
    
    def render(self):
        return "GITHUB"
