#!/usr/bin/python3
"""Takes as arguments a github repository name
and the owner name and list 10 commits
(from the most recent to oldest) of the repository.
"""


if __name__ == "__main__":
    import requests
    import sys

    url_fmt = 'https://api.github.com/repos/{}/{}/commits'
    url = url_fmt.format(sys.argv[2], sys.argv[1])
    params = {'per_page': 10, 'page': 1}
    res = requests.get(url, params=params)
    commits = res.json()
    for commit in commits:
        print('{}: {}'.format(
            commit['sha'],
            commit['commit']['author']['name']
        ))
