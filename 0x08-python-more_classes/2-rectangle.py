#!/usr/bin/python3
'''module that defines a rectangle object'''


class Rectangle:
    '''defines a rectangle object'''
    def __init__(self, width=0, height=0) -> object:
        '''the constructor
        Args:
            width(int): width
            height(int): height
        Return:
            a new object
        '''
        self.width = width
        self.height = height

    @property
    def width(self):
        '''width getter'''
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''height getter'''
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        '''returns the area of the rectangle'''
        return self.height * self.width

    def perimeter(self):
        '''returns the perimeter of the rectangle'''
        if self.height == 0 or self.width == 0:
            return 0
        return 2 * (self.height + self.width)
