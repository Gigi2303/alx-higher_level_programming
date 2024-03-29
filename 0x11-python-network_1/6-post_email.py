#!/usr/bin/python3

"""
Script that sends a POST request to a URL with an email
parameter and displays the body of the response.
"""

import sys
import requests


def main():
    url = sys.argv[1]
    content = {"email": sys.argv[2]}

    request = requests.post(url, data=content)
    print(request.text)


if __name__ == "__main__":
    main()
