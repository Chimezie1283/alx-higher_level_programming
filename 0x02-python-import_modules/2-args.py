#!/usr/bin/python3

if __name__ == "__main__":
    """Print the number and list of arguments."""
    import sys

    countar = len(sys.argv) - 1
    if countar == 0:
        print("0 arguments.")
    elif countar == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(countar))
    for i in range(countar):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))

