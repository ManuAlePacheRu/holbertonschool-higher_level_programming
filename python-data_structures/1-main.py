#!/usr/bin/python3
element_at = __import__('1-element_at').element_at

my_list = [98, 243]
idx = 0
print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))