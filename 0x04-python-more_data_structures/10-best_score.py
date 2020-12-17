#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    score = 0
    key_list = list(a_dictionary.keys())
    val_list = list(a_dictionary.values())
    for y in val_list:
        if y > score:
            score = 0
    return key_list[score]
