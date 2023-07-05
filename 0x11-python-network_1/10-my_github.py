#!/usr/bin/python3
"""Takes Github credentials (username & password) of a user
and uses the GitHub API to display your id
"""

if __name__ == "__main__":
    import requests
    import sys

    url = "https://api.github.com/users/{}".format(
            sys.argv[1]
            )
    headers = {
        'Authorization': "{}".format(sys.argv[2]),
        'X-GitHub-Api-Version': '2022-11-28'
    }
    res = requests.get(url, headers)
    if res.status_code >= 400:
        print(None)
    else:
        user = res.json()
        print(user.get('id', None))
