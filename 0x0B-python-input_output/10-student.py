#!/usr/bin/python3
''' Module for Student class '''


class Student:
    ''' Representaton of a Student '''

    def __init__(self, first_name, last_name, age):
        ''' Instantiation '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        ''' Retrieves dictionary representation '''
        if type(attrs) is list and all([type(x) == str for x in attrs]):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        else:
            return self.__dict__.copy()
