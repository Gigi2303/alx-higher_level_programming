#!/usr/bin/python3

"""
This sends a request to a URL and displays the body of the response
(decoded in utf-8). Handles urllib.error.HTTPError exceptions
and prints the HTTP status code.
"""

import urllib.request
import urllib.error
import sys


def main():
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))


if __name__ == "__main__":
    main()
