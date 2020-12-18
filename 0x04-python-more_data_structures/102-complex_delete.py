#!/usr/bin/python3
def complex_delete(dic, value):
    for x, y in dic.items():
        if y == value:
            dic.pop(value, None)
    return dic
