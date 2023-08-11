#!/usr/bin/python3

""" prints the sum of 1 and two """

from add_0 import add

if __name__ == "__main__":
    a = 1
    b = 2
    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
