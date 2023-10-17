#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    numba = 0
    denz = 0

    for tup in my_list:
        numba += tup[0] * tup[1]
        denz += tup[1]

    return (numba / denz)
