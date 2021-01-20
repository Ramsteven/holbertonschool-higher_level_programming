#!/usr/bin/python3
'''module square#1'''
Rectangle = __import__("9-rectangle").Rectangle


class Square:
    '''
    Square class super implentation
    '''
    def __init__(self, size):
        ''' initialize the class '''
        self.integer_validator("size", size)
        super().__init__ (size, size)
        self.__size = size

    def area(self):
        ''' area method '''
        return self.__size ** 2

    def __str__(self):
        ''' __str__ method '''
        return "[Square] " + str(self.__size) + "/" + str(self.__size)
