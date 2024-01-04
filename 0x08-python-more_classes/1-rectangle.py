#!/usr/bin/python3
"""Below is a Rectangle class"""


class Rectangle:
    """Below the class has been intialized"""
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def width(self):
        """Making width variable private"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setting some conditionals for width"""
        if not isinstance(value, int):
            raise TypeError("width should be an integer")
        if value < 0:
            raise ValueError("width should be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @width.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height should be an integer")
        if value < 0:
            raise ValueError("height should be > 0")
        self.__height = value
