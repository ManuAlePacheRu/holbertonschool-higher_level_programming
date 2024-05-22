#!/usr/bin/python3

def say_my_name(first_name, last_name=""):
    """
    Print the provided first and last names.

    Args:
        first_name (str): The first name to be printed.
        last_name (str, optional): The last name to be printed. Defaults to "".

    Raises:
        TypeError: If either first_name or last_name is not a string.
    """
    """ Check if first_name is a string """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    
    """ Check if last_name is a string """
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    
    """ Print the name """
    print("My name is {} {}".format(first_name, last_name))
