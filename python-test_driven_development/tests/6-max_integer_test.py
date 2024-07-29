#!/usr/bin/python3

"""5 TEXT INDETATIONN"""


def text_indentation(text):
    """
    Insert two new lines after each of the specified characters in the text.

    Parameters:
    text (str): The text to process. It must be a string.

    Raises:
    TypeError: If the input text is not a string.

    Returns:
    None
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    busca = ['.', '?', ':']
    for char in text:
        if char not in busca:
            print(char, end='')
        else:
            print(char)
            print()
