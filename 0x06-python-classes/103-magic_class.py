#!/usr/bin/python3

"""Circle Module"""


import math


class MagicClass:
    """Circle Class

    Attributes:
        __radius (int|float): The raduis of the circle.
    """

    def __init__(self, radius=0):
        """Instantiates a new Circle given its radius

        Args:
            radius (int|float): the radius of the circle.
        """
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")

        self.__radius = radius

    def area(self):
        """Calculates and return the area of the circle"""
        return (math.pi * (self.__radius ** 2))

    def circumference(self):
        """Calculates and return the circumference` of the circle"""
        return (2 * math.pi * self.__radius)
