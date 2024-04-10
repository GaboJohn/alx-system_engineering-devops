#!/usr/bin/python3
'''
function that queries the Reddit API and returns
the number of subscribers
'''

import requests


def number_of_subscribers(subreddit):
    ''' Reddit API endpoint for subreddit info '''

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    headers = {'User-Agent': 'MyBot/1.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()

        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0
