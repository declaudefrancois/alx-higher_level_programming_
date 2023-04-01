#!/usr/bin/python3
"""
    List 10 commits (from the most recent to oldest) of the repository
    “rails” by the user “rails” using github api.
"""
import sys
import requests


if __name__ == "__main__":
    url_fmt = "https://api.github.com/repos/{}/{}/commits"
    res = requests.get(
            url_fmt.format(sys.argv[2], sys.argv[1]),
            params={'per_page': 10, 'page': 1},
            headers={'X-GitHub-Api-Version': '2022-11-28'}
        )
    try:
        commits = res.json()
        fmt = "{}: {}"
        for commit in commits:
            print(fmt.format(
                commit['sha'],
                commit['commit']['author']['name']
            ))
    except Exception as e:
        print(e)
