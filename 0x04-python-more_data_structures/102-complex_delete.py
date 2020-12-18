#!/usr/bin/python3
def complex_delete(dic, value):
    values = list(dic.values())
    keys = list(dic.keys())
    for i in values:
        if i == value:
            position = values.index(i)
            dic.pop(keys[position], 0)
    return dic
