#!/usr/bin/python3
"""How many subscribers"""

import requests


def number_of_subscribers(subreddit):
    """
        gets number of subs
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "custom user agent"}
    req = requests.get(url, headers=headers, allow_redirects=False)
    if req.status_code == 404:
        return 0
    data = req.json().get("data")
    return data.get("subscribers")
