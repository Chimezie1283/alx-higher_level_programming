#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_list = set(my_list)
    numba = 0

    for i in unique_list:
        numba += i

    return (numba)
