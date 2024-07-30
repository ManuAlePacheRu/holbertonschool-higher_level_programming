#!/usr/bin/python3

"""
    Class Mylist and print sorted method
"""


class MyList(list):
    """
        Class creation
    """
    def print_sorted(self):
        """
            My list module sorted list
        """
        sorted_list = sorted(self)
        print(sorted_list)
