#!/usr/bin/python3
'''
contains a function that echoes a given name
'''


def say_my_name(first_name, last_name=""):
    '''prints the full name in a sentence
    Args:
        first_name(str): first name
        last_name(str): last name (optional)
    Return:
        nothing
    '''
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
