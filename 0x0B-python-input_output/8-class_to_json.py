#!/usr/bin/python3
''' Module for class_to_json func '''


def class_to_json(obj):
    if hasattr(obj, "__dict__"):
        return obj.__dict__.copy()
    else:
       return {}
