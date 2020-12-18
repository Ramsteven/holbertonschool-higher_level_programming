#!/usr/bin/python3
def complex_delete(dic, value):
    dictio = dic.copy()
    for x, y in dictio.items():
        if y == value:
            del dic[x]
    return dic
