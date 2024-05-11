#!/usr/bin/python3
def uppercase(str):
    upperstr = ''
    for char in str:
        if 'a' <= char <= 'z':
            upperstr += chr(ord(char) - ord('a') + ord('A'))
        else:
            upperstr += char
    print(upperstr, end="")
    print()
