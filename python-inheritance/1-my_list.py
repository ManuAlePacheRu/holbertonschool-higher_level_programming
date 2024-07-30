#!/usr/bin/python3

"""
Class Mylist and print sorted method
"""


class Mylist(list):
    """
    Class creation
    """
    def print_sorted(self):
        """sorted list"""
        sorted_list = sorted(self)
        print(sorted_list)
