#!/usr/bin/python3
"""Contains recurse function"""
import requests


def recurse(subreddit, hot_list=None, after=None):
    """
    Recursively queries the Reddit API to retrieve all
    hot articles for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to
        retrieve hot articles from.
        hot_list (list): A list to accumulate the titles of
        hot articles (default None).
        after (str): A token indicating the start of the next
        page of results (default None).

    Returns:
        list: A list containing the titles of all hot articles
        for the given subreddit,
              or None if the subreddit is not valid or no
              results are found.
    """
    if hot_list is None:
        hot_list = []

    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {'User-Agent': 'MyScript/1.0'}

    params = {'limit': 100}

    if after:
        params['after'] = after

    try:
        response = requests.get(url, headers=headers,
                                params=params, allow_redirects=False)
        response.raise_for_status()

        data = response.json()
        posts = data['data']['children']

        hot_list.extend([post['data']['title'] for post in posts])

        after = data['data'].get('after')
        if after:
            recurse(subreddit, hot_list, after)

    except requests.RequestException:
        return None

    except KeyError:
        return None

    return hot_list if hot_list else None
