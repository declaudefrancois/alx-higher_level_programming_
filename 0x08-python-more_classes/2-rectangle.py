#!/usr/bin/python3
"""
    This module a single class representing
    a rectangle.
"""


class Rectangle:
    """
        Represents a reactangle.

        Args:
            width (int): the reactangle width.
            height (int): the rectangle height.

        Attributes:
            width (int): the reactangle width.
            height (int): the reactangle height.
    """

    def __init__(self, width=0, height=0):
        """
            Instanciates a new Rectangle.

            Args:
                width (int): the reactangle width.
                height (int): the rectangle height.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
            Getter of the rectangle's width.

            Returns:
                int: The rectangle's width.
        """
        return self.__width

    @width.setter
    def width(self, width):
        """
            Setter of the recatangle width.

            Args:
                width (int): the rectangle width to set.
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")

        if width < 0:
            raise ValueError("width must be >= 0")

        self.__width = width

    @property
    def height(self):
        """
            Getter of the rectangle's height.

            Returns:
                int: The rectangle's height.
        """
        return self.__height

    @height.setter
    def height(self, height):
        """
            Setter of the recatangle width.

            Args:
                height (int): the rectangle width to set.
        """
        if type(height) is not int:
            raise TypeError("height must be an integer")

        if height < 0:
            raise ValueError("height must be >= 0")

        self.__height = height

    def area(self):
        """
            Calcualtes and returns the area of the rectangle
            instance.

            Returns:
                int: the reactangle's area.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
            Calculates and returns the perimeter of the rectangle
            instance.

            Returns:
                int: The rectangle instance perimeter.
        """
        if self.width == 0 or self.height == 0:
            return 0

        return 2 * (self.__width + self.__height)
