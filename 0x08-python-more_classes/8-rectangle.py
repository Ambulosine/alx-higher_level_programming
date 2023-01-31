#!/usr/bin/python3
'''module that defines a rectangle object'''


class Rectangle:
    '''defines a rectangle object'''
    number_of_instances = 0
    print_symbol = '#'

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
        Rectangle.number_of_instances += 1

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

    def area(self) -> int:
        '''returns the area of the rectangle'''
        return self.height * self.width

    def perimeter(self) -> int:
        '''returns the perimeter of the rectangle'''
        if self.height == 0 or self.width == 0:
            return 0
        return 2 * (self.height + self.width)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        '''compares two rectangles
        Args:
            rect_1(Rectangle): first rect
            rect_2(Rectangle): second rect
        Return:
            the bigger of the two
        '''
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() > rect_2.area():
            return rect_1
        elif rect_2.area() > rect_1.area():
            return rect_2
        else:
            return rect_1

    def __str__(self) -> str:
        '''string representation of the rectangle using #'''
        rep_str = ""
        if self.height == 0 or self.width == 0:
            return rep_str
        for i in range(self.height):
            for j in range(self.width):
                rep_str += str(self.print_symbol)
            if i != self.height - 1:
                rep_str += '\n'
        return rep_str

    def __repr__(self) -> str:
        '''return a reversible string representation of the rectangle'''
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        '''prints a message when a rectangle is deleted'''
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
