#!/usr/bin/python3
'''definition is_ind_of_class function'''


def inherits_from(obj, a_class):
    '''
    function kind
    '''

    return issubclass(type(obj), a_class) and type(obj) is not a_class
