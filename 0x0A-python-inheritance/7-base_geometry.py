#!/usr/bin/python3
""" class methond """


class BaseGeometry:
    '''
    BaseGeometry
    '''
    def area(self):
        ''' area method '''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        ''' define a integer validator method '''
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name +" must be greater than 0")
