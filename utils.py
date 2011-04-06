def curry(_curried_function, *args, **kwargs):
    def _curried(*extraargs, **extrakwargs):
        return _curried_function(*(args + extraargs), **dict(kwargs, **extrakwargs))
    return _curried

def service(service_type, **kwargs):
    
    if not service_type:
        return None
    else:
        name = kwargs.get("name", service_type)
        title = kwargs.get("title", service_type.title())
        extra = kwargs.get("extra", {})
        return (service_type, name, title, extra,)
