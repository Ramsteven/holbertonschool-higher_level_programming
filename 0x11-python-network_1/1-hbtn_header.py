#!/usr/bin/python3
# Send a request to the URL

from sys import argv
from  urllib import request

try:
    with request.urlopen(argv[1]) as header:
       print(header.info()['X-Request-Id'])
except Exception as err:
    pass
