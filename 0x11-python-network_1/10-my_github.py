#!/usr/bin/python3
"""Takes your GitHub credentials (username and password)
- uses the GitHub API to display your id.
"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    url = "https://api.github.com/user"
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    r = requests.get(url, auth=auth)
    print(r.json().get("id"))
