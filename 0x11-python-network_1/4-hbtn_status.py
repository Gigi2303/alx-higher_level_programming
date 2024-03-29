#!/usr/bin/python3

"""
A script that Fetches the status from https://alx-intranet.hbtn.io/status
using the requests package.
"""

import requests


def main():
    url = "https://alx-intranet.hbtn.io/status"
    response = requests.get(url)
    content = response.text

    print("Body response:")
    print("\t- type:", type(content))
    print("\t- content:", content)


if __name__ == "__main__":
    main()
