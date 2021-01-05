#!/usr/bin/python3
'''square class'''


class Square:
    '''init square and raising errors'''
    def __init__(self, size=0, position=(0, 0)):
        if type(size) is not int or \
           type(position[0]) is not int or \
           type(position[1]) is not int:
            raise TypeError("size must be an integer")
        elif size < 0 or position[0] < 0 or position[1] < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        self.__position = position
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
        if self.__position:
            for x in range(self.__position[1]):
                print()
        if self.size == 0:
            print()
            return
        for y in range(0, self.__size):
            for x in range(0, self.__position[0]):
                print(" ", end="")
            for x in range(0, self.__size):
                print("#", end="")
            print()
    '''position getter'''
    @property
    def position(self):
        return self.__position
    ''' position setter'''
    @position.setter
    def position(self, value):
        if type(value) is not tuple or type(value[1]) is not int or \
           type(value[0]) is not int or value[0] < 0 or value[1] < 0 or \
           len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
