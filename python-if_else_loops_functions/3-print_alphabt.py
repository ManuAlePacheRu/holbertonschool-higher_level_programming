#!/usr/bin/python3
for charpos in range(ord('a'), ord('z')+1):
    char = chr(charpos)
    if charpos == ord('e') or charpos == ord('q'):
        continue
print("{}".format(char), end='')
