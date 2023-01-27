#!/usr/bin/python3
'''
contains a function that prints two newlines after any of
these characters: '.', '?', and ':'
'''


def text_indentation(text):
    '''adds a 2 newlines after '.', '?', and ':'
    Args:
        text(str): string to be printed
    Return:
        nothing
    '''
    res_str = ""
    if type(text) is not str:
        raise TypeError("text must be a string")
    i = 0
    while i < len(text):
        if text[i] in ['.', '?', ':']:
            res_str += text[i]
            res_str += "\n\n"
            if i + 1 < len(text) and text[i + 1] == " ":
                i += 1
        else:
            res_str += text[i]
        i += 1
    print(res_str, end="")
