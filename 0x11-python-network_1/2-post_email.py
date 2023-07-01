#!/usr/bin/python3
"""That takes in a URL and an email, sends a POST request to
the passed URL with the email as a parameter, and display
the body of the response (decoded in utf-8).
"""


if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    import sys

    url = sys.argv[1]
    data = urllib.parse.urlencode({'email': sys.argv[2]})
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        res_content = response.read()
        print(res_content.decode())
