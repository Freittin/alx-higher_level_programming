#!/usr/bin/python3
'''Module for Square class.'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    ''' subclass representign a Square '''

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        ''' returns the area of Square '''
        return self.__size ** 2

    def __str__(self):
        '''Returns string representation of this square.'''
        return "[Square] " + str(self.__size) + "/" + str(self.__size)
