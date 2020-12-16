#!/usr/bin/python3
def multiple_returns(sentence):
    if not isinstance(sentence, str):
        return None
    tuple_new = (len(sentence), sentence[0])
    return tuple_new
