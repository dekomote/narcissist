# -*- coding: utf-8 -*

"""
narcissist.utils
----------------

Holds utility functions used across the package.

"""

def curry(_curried_function, *args, **kwargs):
    """ The force! Trust it """

    def _curried(*extraargs, **extrakwargs):
        return _curried_function(*(args + extraargs), **dict(kwargs, **extrakwargs))
    return _curried

def service(service_module, **kwargs):
    """ Utility function that returns a service tuple """
    
    if not service_module:
        return None
    else:
        plugin = kwargs.get("plugin", service_module.split(".")[-1]).lower()
        name = kwargs.get("name", plugin)
        title = kwargs.get("title", plugin.title())
        extra = kwargs.get("extra", {})
        return (service_module, plugin,  name, title, extra,)
