#!/usr/bin/python3
def complex_delete(dic, value):
    values = list(dic.values())
    keys = list(dic.keys())
    for i in values:
        if i == value:
            position = values.index(value)
            key = keys[position]
            dic.pop(key, 0)
    return dic
