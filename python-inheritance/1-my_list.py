#!/usr/bin/python3
"""Class Mylist and print sorted method"""


class Mylist(list):
    """class creation"""
    def print_sorted(self):
        """sorted list"""
        print(sorted(self))
