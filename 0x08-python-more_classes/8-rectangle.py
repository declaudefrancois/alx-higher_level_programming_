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
            number_of_instances(int): Number of instances of the class.
            print_symbol (any): symbol for string representation.
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
            Instanciates a new Rectangle.

            Args:
                width (int): the reactangle width.
                height (int): the rectangle height.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
            Returns the biggest rectangle, the one with
            the biggest area.

            Args:
                rect_1 (Rectangle): the first Rectangle.
                rect_2 (Rectangle): the second Rectangle.

            Returns:
                Rectangle: The Rectangle wit hthe biggest area.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() == rect_2.area():
            return rect_1

        return rect_1 if rect_1 > rect_2 else rect_2

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
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
            Return a human readable formatted string
            of the rectangle instance.
        """
        if self.width == 0 or self.width == 0:
            return ""

        str_rep = ""
        for i in range(self.height):
            for j in range(self.width):
                str_rep += "{}".format(self.print_symbol)
            str_rep += "\n" if i < self.height - 1 else ""
        return str_rep

    def __repr__(self):
        """
            Return a conventional string represnting
            the reactangle instance.
        """
        if self.width == 0 or self.width == 0:
            return ""
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def __eq__(self, other):
        """
            Magic method to use for == or
            != comparison between two Rectangles.
        """
        return self.width == other.width and self.height == other.height

    def __gt__(self, other):
        """
            Magic method to use for > comparison
            between two Rectangles.
        """
        return self.area() > other.area()
