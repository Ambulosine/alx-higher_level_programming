#!/usr/bin/python3
def no_c(string):
    for char in string:
        if char == 'C' or char == 'c':
            string = string.split(char)
            string = ''.join(string)
    return string
