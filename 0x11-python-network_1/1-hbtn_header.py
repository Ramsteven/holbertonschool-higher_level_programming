#!/usr/bin/python3
""" this a function that print x-request-id gives a response """


from sys import argv
from urllib import request

try:
    with request.urlopen(argv[1]) as header:
        print(header.info()['X-Request-Id'])
except Exception as err:
    pass
