#!/usr/bin/python3
'''square class'''


class Square:
    '''init square and raising errors'''
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
    '''get value area'''
    def area(self):
        return self.__size**2
    '''setter size '''
    @property
    def size(self):
        return self.__size
    '''set size'''
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
    ''' print ouput of the square '''
    def my_print(self):
        for y in range(0, self.__size):
            for x in range(0, self.__size):
                print("#", end="")
            print()
