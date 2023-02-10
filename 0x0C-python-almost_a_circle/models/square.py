#!/usr/bin/python3
'''define square objects'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''class to define square objects'''

    def __init__(self, size, x=0, y=0, id=None, test=False):
        super().__init__(size, size, x=x, y=y, id=id, test=test)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        '''assigns new values to the square attributes using *args'''
        attr_list = ["id", "size", "x", "y"]
        if args is not None and len(args) > 0:
            if len(args) <= len(attr_list):
                attr_list = attr_list[:len(args)]
            for i in range(len(attr_list)):
                self.__update_attr(i, args[i])
            return

        attr_list = ["id", "size", "x", "y"]
        for key, value in kwargs.items():
            try:
                index = attr_list.index(key)
            except ValueError:
                continue
            self.__update_attr(index, value)

    def __update_attr(self, index, value):
        '''convinience method to set attrs from within update() method'''
        if index == 0:
            self.id = value
        elif index == 1:
            self.width = value
            self.height = value
        elif index == 2:
            self.x = value
        elif index == 3:
            self.y = value

    def to_dictionary(self) -> dict:
        '''returns a dict of the square object attributes'''
        attr_dict = {}
        attr_dict['id'] = self.id
        attr_dict['size'] = self.width
        attr_dict['x'] = self.x
        attr_dict['y'] = self.y
        return attr_dict

    def __str__(self):
        '''string representation of a square obj'''
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
