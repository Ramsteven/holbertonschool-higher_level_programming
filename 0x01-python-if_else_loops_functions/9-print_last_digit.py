#!/usr/bin/python3
def print_last_digit(number):
    neoNumber = abs(number);
    if neoNumber > 0:
        neoNumber = neoNumber % 10
    elif neoNumber == 0:
        neoNumber = 0
    print("{:d}".format(neoNumber), end = "")
    return neoNumber
    
