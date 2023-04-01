#!/usr/bin/python3
"""
    fetches https://alx-intranet.hbtn.io/status
    and prints info about the response
"""
import requests

if __name__ == "__main__":
    res = requests.get("https://alx-intranet.hbtn.io/status")
    fmt = ("Body response:\n\t"
           "- type: {}\n\t"
           "- content: {}")
    res.encoding = 'utf-8'
    print(fmt.format(
            type(res.text),
            res.text
        ))
