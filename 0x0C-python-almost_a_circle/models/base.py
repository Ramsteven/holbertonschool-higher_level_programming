#!/usr/bin/python3
""" module of Class parent """

import json
import csv


class Base:
    """
        Definition a class base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        constructor of Base class
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ stacticmethod that change a dictionary to json string"""
        if list_dictionaries is None or not list_dictionaries:
            return []
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ class method that allow save one list inside of a file """
        lista = []
        if list_objs is None:
            with open("{}.json".format(cls.__name__),
                      mode="w", encoding="utf-8") as file:
                file.write([])
        else:
            for x in list_objs:
                lista.append(cls.to_dictionary(x))

            with open("{}.json".format(cls.__name__),
                      mode="w", encoding="utf-8") as file:
                file.write(Base.to_json_string(lista))

    def from_json_string(json_string):
        """ method that take a json_string and return python object"""
        if json_string is None or len(json_string) < 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        class method  that take a class and one dictionary
        and return a intance new with this arguments
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(2, 2)

        elif cls.__name__ == "Square":
            dummy = cls(2)

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        class method that load from a file text and change of string to
        elements that full in one dictionary thar create a list of instances
        """
        lista = []
        try:
            with open("{}.json".format(cls.__name__)) as file:
                cosas = cls.from_json_string(file.read())

                for value in cosas:
                    lista.append(cls.create(**value))
                return lista

        except Exception:
            return lista

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ save a list insede of csv file"""
        lista = []
        with open("{}.csv".format(cls.__name__), "w") as file:
            for elements in list_objs:
                lista.append(cls.to_dictionary(elements))
            file.write(cls.to_json_string(lista))

    @classmethod
    def load_from_file_csv(cls):
        """ load file from csv"""
        lista = []
        try:
            with open("{}.csv".format(cls.__name__), encoding="utf-8") as file:
                readFile = cls.from_json_string(file.read())
                for elements in readFile:
                    lista.append(cls.create(**elements))
                return lista
        except Exception:
            return list_objts
