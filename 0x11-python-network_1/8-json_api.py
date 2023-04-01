#!/usr/bin/python3
"""
    Takes in a letter and sends a POST request to
    http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import requests
import sys


if __name__ == "__main__":
    q = sys.argv[1] if len(sys.argv) > 1 else ""
    res = requests.post("http://0.0.0.0:5000/search_user", data={'q': q})
    try:
        res_body = res.json()
        if len(res_body) == 0:
            print("No result")
        else:
            print("[{}] {}".format(
                res_body['id'],
                res_body['name']
            ))
    except Exception as e:
        print(e)
        print("Not a valid JSON")
