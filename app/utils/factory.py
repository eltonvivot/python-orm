import sys

def str_to_class(name):
    return getattr(sys.modules[__name__], name)

def str_to_instance(name):
    return str_to_class(name)()