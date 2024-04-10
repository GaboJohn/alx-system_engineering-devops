#!/usr/bin/python3
'''
function that queries the Reddit API and prints
the titles of the first 10 hot posts listed for
given subreddit.
'''

import requests
import time


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts

    Args:
        subreddit (str): The name of the subreddit to retrieve hot posts from.

    Returns:
        None
    """
    user = {'User-Agent': 'GaboJohn'}
    url = requests.get('https://www.reddit.com/r/{}/about.json'
                       .format(subreddit), headers=user).json()
    try:
        return url.get('data').get('subscribers')
    except Exception:
        return 0


if __name__ == "__main__":
    number_of_subscribers(argv[1])
