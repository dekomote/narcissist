++++++++++
NARCISSIST
++++++++++

Narcissist is open source personal info web application / web service
aggregator with a simple plugin system. Something like about.me/flavors.me
for tech savvy people.

Installing the library
======================

If you have setuptools installed, the requirements will be processed automatically.
Otherwise, the requirements are listed in requirements.txt, so it's easy to
install with pip. After that, install the narcissist package.

Checkout the repo and do
    
    python setup.py install


To see if the library is installed, open up a python shell and try

    from narcissist import app

If all goes well, you can start with your app.

Personalization and deployment
==============================

There's a script for creating project templates, bundled with the package called
narcissist_create. To start with a project, simply call the script with the
project name as an argument:

    narcissist_create [project name]

The script creates a project in your current directory. If you want to create a
project in other directory, use the --dir option.

Adding services to your app
---------------------------

Settings file holds a setting called SERVICES. Inside that setting we define
so called "services". Each service is defined by a module where it resides;
Currently we only have narcissist.services.page and narcissist.services.twitter
The services are autoloaded. Service **name** is for assigning unique names to
same services. If you want 2 different twitter services, set this different
in both. **Title** argument is used for the link that is added on the side.
**Extra** is a dict that's passed to each service. You can put anything you need 
for your service there. Narcissist assumes that your class name is same as 
your module name with Capital case. If that's not the case, you can use the 
attribute **plugin** to set the class name of the plugin. Each service 
inherits from narcissist.services.service.Service class, should implement the 
function render (which should return a string that will be rendered to the
content part of the page).

Inside the "example" dir, you will see a github.py module - an example service
plugin. Inside services there's a line that reads:

    service("github", name="github", title = "My Github")

With this line, the module github will be loaded, and you will have a link
"My Github" in the menu.

Adding Pages to your app
------------------------

To add pages to your app, you will have to use the bundled "page" service.

First you will need to make a new html file that will hold the content. Lets call this i_rock.html.
Put some content in it (all html markup goes) and save it in the templates folder or any subfolder in there.
Then simply add this line to your settings.py:

    service("narcissist.services.page", name = "i_rock", title = "I Rock!" , extra = {"file": "templates/i_rock.html"})

in the services tupple. The argument "name" will be the url of this page so [server]/i_rock will go to this page.
The title will set the page title and the title of the link which shows in the menu on the left.

Adding Twitter profiles to your app
-----------------------------------

Adding twitter profiles to your app is VERY easy. Just add this line:

    service("narcissist.services.twitter", name = "[the name of this endpoint -- also url]", title = "[title of the link]",extra = {"username": "[your username]"},)

in the SERVICES tupple. You can have as many twitter profiles as you want.


Developing Services
===================

Narcissist was built around the idea that everyone can make a service, drop it in a folder and just reference to it.
To build your own service, check on this example:

Open up a file called foo.py - the file name and the class name should be the same, but please - lowercase files, CamelCase classes.


    from narcissist import services

    # your service class has to inherit from services.Service mixin

    class Foo(services.Service):
        """ Foo Service - renders 'Bar' on the web page """

        def __init__(self, extra):
            # extra should always be passed as an argument.

            # We pass extra context/vars/anything we need to get it working.
            
            # since Service is a mixin, no parent construction is done here.
            
            self.extra = extra

        def render(self):            
            # render is the method that is called when we go to the url where this class is registered.
            
            # Here you can return fully rendered HTML, or plain strings            
            
            return "Bar"

You are free to add as much functionality as you need e.g. implement a parse_feed function that will parse a feed that will be
passed in "extra" dict and render html with the values parsed. There is no limit here.

In order to get this service in the code, put it in your project path (plugins dir is encouraged) and add the next line in
settings.py in SERVICES section:

    service("plugins.foo", name = "foo", title = "My new Foo service", extra = {},)

This will add a link to the menu called "My new Foo service" that will go to the [host]/foo url and will render "Bar" on the page.