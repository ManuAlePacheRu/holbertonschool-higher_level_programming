 #!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    ソート辞書 = sorted(a_dictionary)
    for 鍵 in ソート辞書:
        print("{}: {}".format(鍵, a_dictionary[鍵]))
