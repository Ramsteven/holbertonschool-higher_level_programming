#!/usr/bin/python3
""" module square children of Rectangle"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".\
                 format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """Accesor method"""
        return self.width

    @size.setter
    def size(self, x):
        """Accesor method"""
        super().__init__(x, x)

    def update(self, *args, **kwargs):
        """Update the values of the instance"""
        size = 0
        if args is not None and len(args) is not 0:
            if len(args) > 2:
                args = list(args)
                args.insert(2, args[1])
                args = tuple(args)
            super().update(*args)
        else:
            keyValue = "size"
            if keyValue in kwargs:
                size = kwargs.get("size")
                kwargs["height"] = size
                kwargs["width"] = size
                kwargs.pop(keyValue)
            super().update(**kwargs)

    def to_dictionary(self):
        """
        method thar return a dictionary with
        the values inside of instance
        """
        d_squ = {}
        d_squ["id"] = getattr(self, "id")
        d_squ["size"] = getattr(self, "width")
        d_squ["x"] = getattr(self, "x")
        d_squ["y"] = getattr(self, "y")
        return(d_squ)
