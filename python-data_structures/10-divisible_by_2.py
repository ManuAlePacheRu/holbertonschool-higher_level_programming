#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    copylist = my_list.copy()
    return [num % 2 == 0 for num in copylist]
