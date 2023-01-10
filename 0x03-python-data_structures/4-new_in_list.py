#!/usr/bin/python3
def new_in_list(the_list, idx, element):
    new_list = the_list.copy()
    if idx < 0:
        return new_list
    elif idx >= len(the_list):
        return new_list
    else:
        new_list[idx] = element
        return 
