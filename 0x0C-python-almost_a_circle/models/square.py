#!/usr/bin/python3
"""
    Contains the Square class.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
        A rectangle with each side equals to each
        other.
        Inherits Rectangle.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
            Instantiata a new Square object.

            Args:
                size (int): The length of a side.
                x (int): horizontal coordinate in a 2d plan.
                y (int): vertical coordinate in a 2d plan.
                id (int): The id of the object.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        fmt = "[{}] ({}) {}/{} - {}"
        return fmt.format(self.__class__.__name__, self.id, self.x,
                          self.y, self.width)

    @property
    def size(self):
        """
            Square's size getter.
        """
        return self.width

    @size.setter
    def size(self, size):
        """
            Square's size setter.

            Args:
                size (int): The Square's side lenght.
        """
        if type(size) is not int:
            self._must_be_int("width")
        if size <= 0:
            self._must_be_gt_0("width")

        self.width = size
        self.height = size
