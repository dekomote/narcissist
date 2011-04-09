from narcissist.services import Service

class Github(Service):
    """ Example service plugin - a future github implementation """
    
    def __init__(self, extra):
        #extra is passed in the constructor
        self.extra = extra
    
    def render(self):
        #what you return here will be rendered on the content page
        return "RENDERED FROM GITHUB PLUGIN"
