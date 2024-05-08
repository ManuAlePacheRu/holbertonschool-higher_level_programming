#!/usr/bin/python3
for i in range(32, 127):
    if chr(i) not in ('e', 'q'):
        print("{}".format(chr(i)), end='')