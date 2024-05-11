#!/usr/bin/python3
def uppercase(str):
    for charpos in range(len(str)):
        if ord(str[charpos]) >= ord('a') and ord(str[charpos]) <= ord('z'):
            print(chr(ord(str[charpos]) - ord('a') + ord('A')), end="")
        else:
            print(str[charpos], end="")
    print()