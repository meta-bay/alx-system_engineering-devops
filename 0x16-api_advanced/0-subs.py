#!/usr/bin/python3
''' How many subscribers'''

import requests


def number_of_subscribers(subreddit):
    '''
    Request number of subs
    '''
    user_agent = 'custom_user_agent'
    url = 'https://www.reddit.com/r/{}.json'.format(subreddit)

    headers = {'User-Agent': user_agent}

    request = requests.get(url, headers=headers, allow_redirects=False)

    if request.status_code != 200:
        return 0

    data = request.json()['data']
    data.get('subscribers')
