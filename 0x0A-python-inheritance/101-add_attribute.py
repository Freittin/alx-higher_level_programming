#!/usr/bin/python3
'''Module for add_attribute method.'''


def add_attribute(obj, name, value):
    '''Method that tests if it can and sets an attribute.'''
    if hasattr(obj, "__dict__") or \
            (hasattr(obj, "__slots__") and name in obj.__slots__):
             setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
