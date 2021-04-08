#!/usr/bin/python3
def find_peak(list_):
    if list_ == []:
        return None
    else:
        max_ = list_[0]
        for item in list_:
            if item > max_:
                max_ = item
        return (max_)
