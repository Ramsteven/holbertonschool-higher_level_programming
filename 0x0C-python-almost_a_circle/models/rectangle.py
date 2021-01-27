#!/usr/bin/python3
""" module of parent class Rectangle inherent of Base and Validator class"""


from models.base import Base
from models.validator import Validator


class Rectangle(Base, Validator):
    """
    Class Rectangle
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        constuctor of class rectangle width, height, x, y and id
        """
        super().compare(width, height, x, y)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """acessor method"""
        return self.__width

    @width.setter
    def width(self, x):
        """acessor method"""
        self.__width = x

    @property
    def height(self):
        """acessor method"""
        return self.__height

    @height.setter
    def height(self, x):
        """acessor method"""
        super().width_height(x, "height")
        self.__height = x

    @property
    def x(self):
        """acessor method"""
        return self.__x

    @x.setter
    def x(self, x):
        """acessor method"""
        super().x_y(x, "x")
        self.__x = x

    @property
    def y(self):
        """acessor method"""
        return self.__y

    @y.setter
    def y(self, y):
        """acessor method"""
        super().x_y(y, "y")
        self.__y = y

    def area(self):
        """method thar return area of a Rectangle o square"""
        return self.__width * self.__height

    def display(self):
        """render of Rectangle or Square !!height=x , width=y, y=z, y=w"""
        for z in range(0, self.__y):
            print()
        for x in range(0, self.__height):
            for w in range(0, self.__x):
                print(" ", end="")
            for y in range(0, self.__width):
                print("#", end="")
            print("\n", end="")

    def __str__(self):
        """method str"""
        return "[Rectangle] ({}) {}/{} - {}/{}"\
            .format(self.id, self.__x, self.__y,
                    self.__width, self.__height)

    def update(self, *args, **kwargs):
        """ method that allow update values of a instance"""
        key = ["width", "height", "x", "y"]

        if args is not None and len(args) is not 0:
            value = args[1:]
            super().__init__(args[0])

            for x in range(len(value)):
                setattr(self, key[x], value[x])
        else:
            for x in kwargs.keys():
                if x is not "id":
                    setattr(self, x, kwargs.get(x))
                else:
                    super().__init__(kwargs.get(x))

    def to_dictionary(self):
        """
        function that take of value of instance
        and create a dictionary with this
        """
        d_rec = {}
        d_rec["id"] = getattr(self, "id")
        d_rec["width"] = getattr(self, "width")
        d_rec["height"] = getattr(self, "height")
        d_rec["x"] = getattr(self, "x")
        d_rec["y"] = getattr(self, "y")
        return(d_rec)
