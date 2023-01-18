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

    def area(self):
        """
            Computes an returns the area of the
            rectangle instance.
        """
        return self.width * self.height

    def display(self):
        """
            Display a Rectangle using #
            symbol as unit. (# = 1)
        """
        print("\n".join(["#" * self.width
                        for i in range(self.height)]))

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
        if type(width) is not int:
            self.__must_be_int("width")
        if width <= 0:
            self.__must_be_gt_0("width")

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
        if type(height) is not int:
            self.__must_be_int("height")
        if height <= 0:
            self.__must_be_gt_0("height")

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
        if type(x) is not int:
            self.__must_be_int("x")
        if x < 0:
            self.__must_be_gte_0("x")

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
        if type(y) is not int:
            self.__must_be_int("y")
        if y < 0:
            self.__must_be_gte_0("y")

        self.__y = y

    def __must_be_int(self, name):
        """
            Throws a typeError formated as :
            "<name> must be an integer."

            Args:
                name (str) : The name of the attribute.
        """
        raise TypeError("{} must be an integer".format(name))

    def __must_be_gte_0(self, name):
        """
            Throws a typeError formated as :
            "<name> must be >= 0"

            Args:
                name (str) : The name of the attribute.
        """
        raise ValueError("{} must be >= 0".format(name))

    def __must_be_gt_0(self, name):
        """
            Throws a typeError formated as :
            "<name> must be > 0"

            Args:
                name (str) : The name of the attribute.
        """
        raise ValueError("{} must be > 0".format(name))

    def __str__(self):
        fmt = "[{}] ({}) {}/{} - {}/{}"
        return fmt.format(self.__class__.__name__, self.id, self.x,
                          self.y, self.width, self.height)
