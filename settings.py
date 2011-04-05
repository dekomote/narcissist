from utils import service


TITLE = "Dejan Noveski"
SUB_TITLE = "This is SPARTAAAAA!"

THEME = "simple"

SERVICES = (
            service("page", name = "index", title = "Bio", 
                extra = {"file": "index.html"}),
            
            service("twitter", name = "dekomote", title = "@dekomote", 
                extra = {"username": "dekomote"},),
            )
