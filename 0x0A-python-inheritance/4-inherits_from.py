#!/usr/bin/python3
''' Module for inherits_from function '''


def inherits_from(obj, a_class):
    '''
    Check if obj is an instance of a that inherited (directly or indirectly)
    from the specified class
    Returns:
        True if obj is an instance of a_class
        False if obj is not an instance of a_class
    '''
    return isinstance(obj, a_class) and type(obj) != a_class
