#!/usr/bin/python3
def number_keys(a_dictionary):
    numba = 0
    list_keys = list(a_dictionary.keys())

    for i in list_keys:
        numba += 1

    return (numba)
