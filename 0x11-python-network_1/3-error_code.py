#!/usr/bin/python3
""" takes in a URL, sends a request to the URL and
displays the body of the response (decoded in utf-8).
"""

if __name__ == "__main__":
    import urllib.error
    import urllib.request
    import sys

    try:
        url = sys.argv[1]
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as response:
            res_content = response.read()
            print(res_content.decode())
    except urllib.error.HTTPError as exception:
        print("Error code: {}".format(exception.code))
