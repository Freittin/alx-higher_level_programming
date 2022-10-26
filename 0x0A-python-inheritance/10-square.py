#!/usr/bin/python3
'''Module for Square class.'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    ''' subclass representing a Square '''

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        ''' returns the area of Square '''
        return self.__size ** 2
