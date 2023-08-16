#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    list_orda = list(a_dictionary.keys())
    list_orda.sort()
    for i in list_orda:
        print("{}: {}".format(i, a_dictionary.get(i))
