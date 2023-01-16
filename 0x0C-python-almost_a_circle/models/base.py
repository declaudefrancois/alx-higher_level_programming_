#!/usr/bin/python3
"""
    Contains the base class of all other
    classes in the project.
"""


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
