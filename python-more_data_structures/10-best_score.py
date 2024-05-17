#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    laux = []
    for score in a_dictionary.values():
        laux.append(score) 
    return max(laux)
