++++++++++
NARCISSIST
++++++++++

Narcissist is open source personal info web application / web service
aggregator with a simple plugin system. Something like about.me/flavors.me
for tech savvy people.

Installing the library
======================

Checkout the repo and do

    python setup.py develop or
    
    python setup.py install

I recommend develop because at the moment, the script is early in
development.

To see if the library is installed, open up a python shell and try

    from narcissist import app

If all goes well, you can start with your app.

Personalization and deployment
==============================

Copy the example dir to a dir of your likings. Inside you can find a file
called settings.py. Open it, edit it. (a paster script is on the way)

Inside the example dir, you will find a wsgi file that can be used with mod_wsgi
and app.py which can be used for other deployment scenarios or just running the
dev server. To run the dev server, call app.py

    python app.py

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
