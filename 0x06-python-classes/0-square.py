#!/usr/bin/python3
class Square:
    """This class represent a square.

    The square is a quadrilateral figure with each side equal to each others.

    Attributes:
        size (int): The size of the square.

    """

    def __init__(self, size=0):
        """Square constructor, instanciate a new Square.

        This function takes an optional size as and initialize the square
        with it.

        Args:
            size (int): The size of the square.

        """
        self.size = size
