#!/usr/bin/python3
class Square:
    """This class represent a square.

    The squre is a quadrilateral figure with each side equal to each others.
    """

    def __init__(self, size=None):
        """Square constructor, instanciate a new Square.

        This function takes an optional size as and initialize the square
        with it.

        Args:
            size (int): The size of the square.
        """

        if size is not None:
            self.size = size
