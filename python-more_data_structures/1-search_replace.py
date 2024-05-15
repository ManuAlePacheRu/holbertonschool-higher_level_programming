#!/usr/bin/python3
def search_replace(my_list, search, replace):
    copylist = my_list.copy()
    for numrep in range(len(copylist)):
        if copylist[numrep] == 2:
            copylist[numrep] = 89
    return copylist
