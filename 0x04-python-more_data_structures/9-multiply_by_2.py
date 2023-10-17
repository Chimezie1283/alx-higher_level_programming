#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_direct = a_dictionary.copy()
    list_keys = list(new_direct.keys())

    for i in list_keys:
        new_direct[i] *= 2

    return (new_direct)
