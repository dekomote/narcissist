from narcissist.utils import service


TITLE = "Dejan Noveski"
SUB_TITLE = "This is SPARTAAAAA!"

THEME = "simple"

SERVICES = (
            service("narcissist.services.page", name = "index", title = "Bio", 
                extra = {"file": "pages/index.html"}),

            service("narcissist.services.twitter", name = "dekomote", title = "@dekomote", 
                extra = {"username": "dekomote"},),
            
            service("github", name="github", title = "My Github"),
            )
