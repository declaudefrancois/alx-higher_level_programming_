#!/usr/bin/python3
"""
    fetches the url given as argument
    and print the value of the X-Request-Id
    header in the response.
"""
from urllib import request
import sys


if __name__ == "__main__":
    with request.urlopen(sys.argv[1]) as res:
        print(dict(res.info()).get("X-Request-Id", None))
