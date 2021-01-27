#!/usr/bin/python3

class Validator():
    def compare(self, width, height, x, y): 
        attr = [width, height, x, y]
        key = ["width", "height", "x", "y"]
        
        for x in range(len(attr)):
            if isinstance(attr[x], int) is not True:
                raise TypeError(key[x] + " must be an integer")
        
        for x in range(len(attr[:2])):
            if attr[x] <= 0:
                raise ValueError(key[x] + " must be > 0")

        for y in range(2, len(attr)):
             if attr[y] < 0:
                raise ValueError(key[y] + " must be >= 0")

    def width_height(self, attribute, name):
        if isinstance(attribute, int) is not True:
            raise TypeError(name + " must be an integer")

        if attribute <= 0:
            raise ValueError(name + " must be > 0")

    
    def x_y(self, attribute, name):
        if isinstance(attribute, int) is not True:
            raise TypeError(name + " must be an integer")
        if attribute < 0:
            raise ValueError(name + " must be >= 0")
