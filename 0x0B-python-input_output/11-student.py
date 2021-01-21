#!/usr/bin/python3
""" module containe class Student """


class Student:
    """
    Class student
    """
    def __init__(self, first_name, last_name, age):
        """ constructor"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ class to json """
        if attrs is None:
            return self.__dict__
        if all(isinstance(at, str) for at in attrs):
            if isinstance(attrs, list):
                return {a: getattr(self, a) for a in attrs if hasattr(self, a)}

    def reload_from_json(self, json):
        '''
        function reload_from_json
        '''
        for key, value in json.items():
            setattr(self, key, value)
