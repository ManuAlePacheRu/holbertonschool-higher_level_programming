#!/usr/bin/python3
for dec in range(0, 9):
    for n in range(1, 10):
        if dec > n or dec == n:
            continue
        if n == 9 and dec ==8:
            print(f"{dec}{n}")
        else:
            print(f"{dec}{n}, ", end="")
