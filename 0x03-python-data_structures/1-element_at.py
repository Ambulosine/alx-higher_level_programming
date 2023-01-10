#!/usr/bin/python3
def element_at(the_list, idx):
    if idx < 0:
        return None
    elif idx >= len(the_list):
        return None
    else:
        return the_list[idx]
