#!/usr/bin/python3
def find_peak(list_of_integers):
    if list_of_integers == []:
        return None
    else:
        max_ = list_of_integers[0]
        for item in list_of_integers:
            if item > max_:
                max_ = item
        return (max_)
