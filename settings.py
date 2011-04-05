from utils import service


TITLE = "Dejan Noveski"
SUB_TITLE = "This is SPARTAAAAA!"

THEME = "simple"

SERVICES = (
            service("page", name = "index", title = "Index", 
                extra = {"file": "index.html"}),
            
            service("twitter", name = "dekomote", title = "My Twitter", 
                extra = {"username": "dekomote"},),
            )
