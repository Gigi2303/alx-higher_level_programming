#!/usr/bin/python3

"""
A Scrpit that Sends a POST request to a URL with an email parameter
        and displays the body of the response (decoded in utf-8).
"""

import sys
import urllib.request
import urllib.parse


def main():
    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({'email': email})
    data = data.encode('utf-8')

    req = urllib.request.Request(url, data=data, method='POST')
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))


if __name__ == "__main__":
    main()
