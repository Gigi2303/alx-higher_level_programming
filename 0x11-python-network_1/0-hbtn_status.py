#!/usr/bin/python3

"""
This module Fetches the status from https://alx-intranet.hbtn.io/status
"""
import urllib.request

if __name__ == "__main__":
     url = 'https://alx-intranet.hbtn.io/status'

    with urllib.request.urlopen(url) as response:
        data = response.read().decode('utf-8')

        print("Body response:")
        print("\t- type: {}".format(type(data)))
        print("\t- content: {}".format(data))
