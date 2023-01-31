#!/usr/bin/python3
'''module that contain a class whose objects prevent dynamic
attribute allocation'''


class LockedClass:
    '''defines an object that cannot be dynamically allocated
    new attributes'''
    __slots__ = ['first_name']
