#!/usr/bin/python3
def islower(c):
        # print(type(c))
        # print(isinstance(c, str))
        if ord(c) <= 122 and ord(c) >= 97:
            return True
        return False
