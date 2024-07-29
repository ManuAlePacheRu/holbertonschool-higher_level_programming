#!/usr/bin/python3
from sys import argv
arg = len(argv)
cant = 0
if arg > 0:
    for i in argv[1:]:
        cant += int(i)
    if __name__ == "__main__":
        print("{}".format(cant))
