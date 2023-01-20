#!/usr/bin/python3
"""
    Contains the base class of all other
    classes in the project.
"""
from json import dumps, loads


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

    @classmethod
    def from_json_string(cls, json_string):
        """
            Returns the list of the JSON string
            representation json_string.

            Args:
                json_string (str): string representing a list of dictionaries.
        """
        if json_string is None or json_string.strip() == "":
            return []
        return loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
            Returns an instance with all attributes already set.

            Args:
                dictionary (dict): keyworded arguments.
        """
        instce = None
        name = cls.__name__
        if name == "Rectangle":
            instce = cls(10, 20)
        else:
            instce = cls(10)

        instce.update(**dictionary)
        return instce

    @classmethod
    def load_from_file(cls):
        """
            Returns a list of instances
            from a json string read in a file.
        """
        with open("{}.json".format(cls.__name__), 'r', encoding="utf-8") as f:
            instces = cls.from_json_string(f.read())
            return [cls.create(**item) for item in instces]
