#!/usr/bin/python3
'''' module list '''


class MyList(list):
    ''' class list '''
    def __init__(self):
        ''' constructor '''
        pass

    def print_sorted(self):
        ''' method sorted '''
        print(sorted(self));
