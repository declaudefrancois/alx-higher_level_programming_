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

    @classmethod
    def save_to_file(cls, list_objs):
        """
            writes the JSON string representation
            of list_objs to a file.

            Args:
                list_objs (list(Base)): ist of instances who inherits of Base.
        """
        lo = []
        cls_name = cls.__name__
        if list_objs is not None:
            lo = [item.to_dictionary()
                  for item in list_objs]
            if len(list_objs) > 0:
                cls_name = list_objs[0].__class__.__name__

        with open("{}.json".format(cls_name), 'w', encoding="utf-8") as f:
            f.write(cls.to_json_string(lo) if type(lo) is list else "")
