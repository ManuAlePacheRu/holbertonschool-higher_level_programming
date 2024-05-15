#!/usr/bin/python3
def search_replace(my_list, search, replace):
    copylist = my_list.copy()
    for numrep in range(len(copylist)):
        if copylist[numrep] == search:
            copylist[numrep] = replace
    return copylist
