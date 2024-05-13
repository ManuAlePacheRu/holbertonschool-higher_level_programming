#!/usr/bin/python3
def no_c(my_string):
    ignorelet = {"c", "C"}
    trans_table = str.maketrans("", "", "".join(ignorelet))
    return my_string.translate(trans_table)
