#!/usr/bin/python3
"""
    fetches the url given as argument
    and print the value of the X-Request-Id
    header in the response.
"""
import requests
import sys


if __name__ == "__main__":
    res = requests.get(sys.argv[1])
    print(res.headers.get('X-Request-Id', None))
