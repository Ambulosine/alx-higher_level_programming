#!/usr/bin/python3
def weight_average(my_list=[]):
    nume = 0
    den = 0
    if my_list:
        for tuples in my_list:
            nume += (tuples[0] * tuples[1])
            den += tuples[1]
        return(nume / den)
    return(0)
