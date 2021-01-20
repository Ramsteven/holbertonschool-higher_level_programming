#!/usr/bin/python3
''' rectangle geometry'''
BaseGeometry = __import__("8-rectangle.py").BaseGeometry

class Rectangle(BaseGeometry):
    '''
        Clas rectangle
    '''
    def __init__(self, width, height):
        ''' constructor '''
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        seld.__height = height
