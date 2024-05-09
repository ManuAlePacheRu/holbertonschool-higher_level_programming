#!/usr/bin/python3
for dec in range(0, 9):
    for n in range(1, 10):
        if dec > n or dec == n:
            continue
        print(f"{dec}{n}, ", end="")