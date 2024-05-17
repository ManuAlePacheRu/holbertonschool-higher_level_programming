#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
   copylist = my_list.copy()
   return list(map(lambda nummul: nummul * number, copylist))
