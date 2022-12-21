#!/usr/bin/python3

"""Square module."""


class Square:
    """This class represents a geometrical square.

    The square is a quadrilateral figure with each side equal to each others.

    Attributes:
        size (int): The size of the square, a positive int.

    """

    def __init__(self, size=0):
        """This method instanciates a new Square.

        Args:
            size (int): The size of the square.
        """
        self.__check_size_value(size)
        self.__size = size

    def __check_size_value(self, size):
        """Checks if a value cannot be used as squre size.

        If the value is compliant, continues otherwise raises an exception.
        Raise a TypeError if value is not int.
        Raise a ValueError if value is less than 0.
        """
        if type(size) != int:
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Calculates the area of the square and returns the result.

        Returns:
            The result of size times size.
        """
        return (self.__size * self.__size)

    @property
    def size(self):
        """Size property getter.

        Returns:
            The value of the square size (int).
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """Sets the size of the square instance.

        Raise an exception if the new value is not int or is less than 0,
        otherwise sets the new value of the square size.

        Args:
            value (int): The new value of the square size to set.
        """
        self.__check_size_value(value)
        self.__size = value

    def my_print(self):
        """Prints the square.

        Prints the square in a two dimensional plane, using the symbol #.
        """
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print("")

        if self.__size == 0:
            print("")
