import importlib

def str_to_class(name, module):
    return getattr(importlib.import_module(module), name)

def str_to_instance(name):
    return str_to_class(name)()