#!/usr/bin/python3
"""
Python script that fetches https://alx-intranet.hbtn.io/status
"""

import requests

url = 'https://intranet.hbtn.io/status'


req = requests.get()
print("Body response:")
print("\t- type: {}".format(type(req.text)))
print("\t- content: {}".format(req.text))
