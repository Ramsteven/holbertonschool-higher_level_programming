#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        return None
    else:
        tuple_new = (len(sentence), sentence[0])
        return tuple_new
