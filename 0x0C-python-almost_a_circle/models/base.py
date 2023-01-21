#!/usr/bin/python3
"""
    Contains the base class of all other
    classes in the project.
"""
from json import dumps, loads
import turtle
from random import randint


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
        try:
            with open("{}.json".format(cls.__name__), 'r',
                      encoding="utf-8") as f:
                instces = cls.from_json_string(f.read())
                return [cls.create(**item) for item in instces]
        except FileNotFoundError as err:
            return []

    @staticmethod
    def to_csv_string(list_dictionaries):
        """
            Returns the csv representation
            of a list of dictionaries.

            Args:
                list_dictionaries (list): List of dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return ""

        str_l = ""
        for d in list_dictionaries:
            str_l += ",".join(["{}".format(v)
                               for k, v in d.items()]) + "\n"
        return str_l

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
            Write a list of Base child instance
            serialized in csv into a csv file.
        """
        lo = []
        cls_name = cls.__name__
        if list_objs is not None:
            lo = [item.to_dictionary()
                  for item in list_objs]
            if len(list_objs) > 0:
                cls_name = list_objs[0].__class__.__name__

        with open("{}.csv".format(cls_name), 'w', encoding="utf-8") as f:
            f.write(cls.to_csv_string(lo) if type(lo) is list else "")

    @classmethod
    def from_csv_string(cls, csv_string):
        """
            Returns the list of dictionaries represented by
            the csv string csv_string.
            Args:
                csv_string (str): string representing a list of dictionaries.
        """
        if csv_string is None or csv_string.strip() == "":
            return []

        csv_rows = csv_string.strip().split("\n")
        instces = []
        for csv_row in csv_rows:
            attrs = csv_row.split(",")
            dictionary = {}
            if len(attrs) == 5:
                for i in range(len(attrs)):
                    value = int(attrs[i])
                    if i == 0:
                        dictionary["id"] = value
                    elif i == 1:
                        dictionary["width"] = value
                    elif i == 2:
                        dictionary["height"] = value
                    elif i == 3:
                        dictionary["x"] = value
                    elif i == 4:
                        dictionary["y"] = value
                instces.append(dictionary)
            elif len(attrs) == 4:
                for i in range(len(attrs)):
                    value = int(attrs[i])
                    if i == 0:
                        dictionary["id"] = value
                    elif i == 1:
                        dictionary["size"] = value
                    elif i == 2:
                        dictionary["x"] = value
                    elif i == 3:
                        dictionary["y"] = value
                instces.append(dictionary)
        return instces

    @classmethod
    def load_from_file_csv(cls):
        """
            Returns a list of instances
            from a json string read from a csv file.
        """
        try:
            with open("{}.csv".format(cls.__name__), 'r',
                      encoding="utf-8") as f:
                instces = cls.from_csv_string(f.read())
                return [cls.create(**item) for item in instces]
        except FileNotFoundError as err:
            return []

    @classmethod
    def _random_colors(self, length):
        """
            Generate a random list of length colors.
        """
        colors = []
        for i in range(length):
            colors.append('#%06X' % randint(0, 0xFFFFFF))
        return colors

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
            Opens a window and draws all
            the Rectangles and Squares.

            Args:
                list_rectangles (list(Rectangle)): list of Rectangle.
                list_squres  (list(Square)): list of Square.
        """
        turtle.Screen()
        turtle.pensize(5)
        turtle.width(5)
        colors = Base._random_colors(len(list_rectangles))
        for i, rect in enumerate(list_rectangles):
            t = turtle.Turtle()
            t.pencolor(colors[i])
            t.speed(1)

            t.pu()
            t.setpos(rect.x, rect.y)
            t.pd()

            t.fd(rect.width)
            t.sety(t.ycor() + rect.height)
            t.bk(rect.width)
            t.sety(t.ycor() - rect.height)

        colors = Base._random_colors(len(list_squares))
        for i, rect in enumerate(list_squares):
            t = turtle.Turtle()
            t.pencolor(colors[i])
            t.speed(1)

            t.pu()
            t.setpos(rect.x, rect.y)
            t.pd()

            t.fd(rect.size)
            t.sety(t.ycor() + rect.size)
            t.bk(rect.size)
            t.sety(t.ycor() - rect.size)
