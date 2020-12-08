#!/usr/bin/python3
def uppercase(str):
    concatenate = ""
    for x in str:
        if ord(x) >= 97 and ord(x) <= 122:
            concatenate += chr(ord(x) - 32)
        else:
            concatenate += x
    print("{:s}".format(concatenate))
