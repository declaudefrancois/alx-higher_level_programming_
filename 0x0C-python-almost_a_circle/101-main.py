#!/usr/bin/python3
""" 101-main """
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

if __name__ == "__main__":

    list_rectangles = [Rectangle(100, 40),
                       Rectangle(90, 110, 30, 10),
                       Rectangle(20, 25, 110, 80)]
    list_squares = [Square(35),
                    Square(15, 26, 5),
                    Square(23, 71, 43),
                    Square(60, 79, 56),
                    Square(78, 70, 78),
                    Square(400, 96, 89),
                    Square(45, 97, 576),
                    Square(10, 9, 502),
                    Square(1, 102, 502),
                    Square(69, 451, 70)]

    Base.draw(list_rectangles, list_squares)
