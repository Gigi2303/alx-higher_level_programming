#!/usr/bin/python3

"""
Uses the GitHub API to display the user ID using Basic Authentication
with a personal access token.
"""

import requests
import sys


def main():
    username = sys.argv[1]
    password = sys.argv[2]

    response = requests.get(
            "https://api.github.com/user", auth=(username, password))

    if response.status_code == 200:
        print(response.json()["id"])
    else:
        print(None)


if __name__ == "__main__":
    main()
