#!/usr/bin/python3
"""
    fetches https://alx-intranet.hbtn.io/status
    and prints info about the response
"""
from urllib import request

if __name__ == "__main__":
    with request.urlopen("https://alx-intranet.hbtn.io/status") as res:
        fmt = ("Body response:\n\t"
               "- type: {}\n\t"
               "- content: {}\n\t"
               "- utf8 content: {}")
        res_content = res.read()
        print(fmt.format(
                type(res_content),
                res_content,
                res_content.decode("utf-8")
            ))
