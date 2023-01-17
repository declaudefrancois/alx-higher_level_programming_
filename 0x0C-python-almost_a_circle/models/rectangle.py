#!/usr/bin/python3
"""
    Rectangle module, contains the
    rectangle class.
"""
from models.base import Base


class Rectangle(Base):
    """
        Represents a closed 2-D shape, having 4 sides
        4 corners, and 4 right angles (90°).

        Attributes:
            __width (int): The width.
            __height (int): The height.
            __x (int): The x coordinate of the rectangle in a 2D plan.
            __y (int): The y coordinate of the rectangle in a 2D plan.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
            Creates a new Rectangle.

            Args:
                width (int): The width.
                height (int): The height.
                x (int): X coordinate.
                y (int): y coordinate.
        """
        super().__init__(id)

        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
            Gets the Rectangle's width.
        """
        return self.__width

    @width.setter
    def width(self, width):
        """
            Sets the Rectangle's width.

            Args:
                width (int): The width value.
        """
        self.__width = width

    @property
    def height(self):
        """
            Gets the Rectangle's height.
        """
        return self.__height

    @height.setter
    def height(self, height):
        """
            Sets the Rectangle's height.

            Args:
                height (int): The height value.
        """
        self.__height = height

    @property
    def x(self):
        """
            Gets the Rectangle's x coordinate.
        """
        return self.__x

    @x.setter
    def x(self, x):
        """
            Sets the Rectangle's x coordinate.

            Args:
                x (int): The x coordinate value.
        """
        self.__x = x

    @property
    def y(self):
        """
            Gets the Rectangle's x coordinate.
        """
        return self.__y

    @y.setter
    def y(self, y):
        """
            Sets the Rectangle's y coordinate.

            Args:
                y (int): The y coordinate value.
        """
        self.__y = y
