#!/usr/bin/python3
"""
    That takes your GitHub credentials (username and password)
    and uses the GitHub API to display your id.
"""
import requests
import sys


if __name__ == "__main__":
    # creds = auth.HTTPBasicAuth(sys.argv[1], sys.argv[2])
    res = requests.get(
        'https://api.github.com/user',
        auth=(sys.argv[1], sys.argv[2]),
        headers={'X-GitHub-Api-Version': '2022-11-28'}
    )
    try:
        if res.status_code >= 400:
            print(None)
        else:
            res_body = res.json()
            print(res_body['id'])
    except Exception as e:
        print(None)
