#!/usr/bin/python3
"""
    Contains the base class of all other
    classes in the project.
"""
from json import dumps


class Base:
    """
        Base class.

        Attributes:
            __nb_objects (int): The number of object.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
            Create a new instance of Base class.

            Args:
                id (int): A number acting as an id for the object.
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """
            eturns the JSON string representation
            of list_dictionaries.

            Args:
                list_dictionaries (list(dict)): List of dict.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return dumps(list_dictionaries)
