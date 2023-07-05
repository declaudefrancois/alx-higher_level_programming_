#!/usr/bin/python3
"""takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

if __name__ == "__main__":
    import requests
    import sys

    url = "http://0.0.0.0:5000/search_user"
    q = sys.argv[1] if len(sys.argv) > 1 else ""
    res = requests.post(url, data={'q': q})
    try:
        d = res.json()
        if len(d) == 0:
            print('No result')
        else:
            print("[{}] {}".format(d['id'], d['name']))
    except Exception as e:
        print('Not a valid JSON')
