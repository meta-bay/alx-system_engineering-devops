#!/usr/bin/python3
"""
hot posts on a subreddit
"""

import requests


def top_ten(subreddit):
    """Print the titles of the 10 hottest posts """
    url = "https://www.reddit.com/r/{}/hot/.json?limit=10".format(subreddit)
    headers = {"User-Agent": "custom agent 2"}
    res = requests.get(url, headers=headers, allow_redirects=False)
    if res.status_code == 404:
        print("None")
        return
    result = res.json().get("data")
    [print(i.get("data").get("title")) for i in result.get("children")]
