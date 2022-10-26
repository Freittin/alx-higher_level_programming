#!/usr/bin/python3
''' Module for Student class '''


class Student:
    ''' Representaton of a Student '''

    def __init__(self, first_name, last_name, age):
        ''' Instantiation '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        ''' Retrieves dictionary representation '''
        return self.__dict__.copy()
