from exceptions import KeyError
registered_services = {}

class Service(object):

    @staticmethod
    def load(name, extra_context):
        try:
            cls = registered_services.get(name)
            return cls(extra_context)
        except KeyError, e:
            return None

    class __metaclass__(type):
        def __init__(cls, name, bases, dict):
            type.__init__(cls, name, bases, dict)
            registered_services[name.lower()] = cls

