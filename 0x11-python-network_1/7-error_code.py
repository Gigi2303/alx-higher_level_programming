#!/usr/bin/python3

"""
This script sends a request to a URL and displays the body of the response.
Prints an error message if the HTTP status code is greater than or equal to 400.
"""

import requests
import sys


def main():
    url = sys.argv[1]

    response = requests.get(url)
    if response.status_code >= 400:
        print("Error code:", response.status_code)
    else:
        print(response.text)


if __name__ == "__main__":
    main()
