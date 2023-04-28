#!/usr/bin/python3
"""
Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""

import requests
import sys


if __name__ == "__main__":
    url = 'https://api.github.com/user'
    req = requests.get(url, auth=(sys.argv[1], sys.argv[2]))
    print(req.json().get('id'))
