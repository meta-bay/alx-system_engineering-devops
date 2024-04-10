#!/usr/bin/python3
"""
a list of all hot posts on a given Reddit subreddit.
"""

import requests


def recurse(subreddit, hot_list=[], the_next=None, count=0):
    """
    Recursively retrieves a list of titles of all hot posts
    on a given subreddit.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "custom agent 3"}
    res = requests.get(url, headers=headers, allow_redirects=False)

    if res.status_code != 200:
        return None

    data = res.json()['data']

    posts = data['children']
    for post in posts:
        count += 1
        hot_list.append(post['data']['title'])

    the_next = data['after']
    if the_next is not None:
        return recurse(subreddit, hot_list, the_next, count)
    else:
        return hot_list
