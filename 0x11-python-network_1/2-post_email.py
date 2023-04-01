#!/usr/bin/python3
"""
    Takes in a URL and an email address.
    sends a POST request to the passed URL with the email as a parameter,
    and displays the body of the response (decoded in utf-8).
"""
from urllib import request, parse
import sys


if __name__ == "__main__":
    body = parse.urlencode({'email': sys.argv[2]})
    body = body.encode('ascii')
    with request.urlopen(sys.argv[1], body) as res:
        print(res.read().decode('utf-8'))
