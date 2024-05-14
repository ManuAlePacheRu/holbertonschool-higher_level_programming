#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    div = my_list[0]
    for i in range(my_list[div]):
        if my_list[i] // 2:
            return True
        else: 
            return False