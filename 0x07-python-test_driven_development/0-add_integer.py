#!/usr/bin/python3
'''contains a function that add integers'''


def add_integer(a: int, b=98) -> int:
    '''adds two integers
    Args:
        a(int): first integer
        b(int/float): second number
    Return:
        int: sum of a and b
    '''
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    return int(a) + int(b)
