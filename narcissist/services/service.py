# -*- coding: utf-8 -*-

"""

narcissist.services.service
---------------------------

Module full of ponies.

"""

from exceptions import KeyError

# registered_services holds the loaded service plugins
registered_services = {}

class Service(object):
    """ Acts as a Factory and as a plugin loader. It's metaclass registers each
        class that inherits it in registered_services """

    @staticmethod
    def load(name, extra_context):
        """ The Factory part """

        try:
            cls = registered_services.get(name)
            return cls(extra_context)
        except KeyError, e:
            return None

    class __metaclass__(type):
        """ PONIES """

        def __init__(cls, name, bases, dict):
            type.__init__(cls, name, bases, dict)
            registered_services[name.lower()] = cls

