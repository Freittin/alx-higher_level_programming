#!/usr/bin/python3
''' Module for is_same_class function '''


def is_same_class(obj, a_class):
    '''
    Check if obj is an instance of a_class
    Returns:
        True if obj is an instance of a_class
        False if obj is not an instance of a_class
    '''
    return type(obj) == a_class
