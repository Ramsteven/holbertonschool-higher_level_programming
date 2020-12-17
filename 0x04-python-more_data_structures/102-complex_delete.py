#!/usr/bin/python3
def complex_delete(dic, value):
    if not value:
        return dic
    values = list(dic.values())
    keys = list(dic.keys())
    if value not in values:
        return dic
    else:
        position = values.index(value)
        key = keys[position]
        dic.pop(key, 0)
    return dic
