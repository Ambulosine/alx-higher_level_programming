#!/usr/bin/python3
def uniq_add(my_list=[]):
    add = 0
    if my_list:
        for i in set(my_list):
            add += i
    return add
