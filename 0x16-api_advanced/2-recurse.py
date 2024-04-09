#!/usr/bin/python3
"""Contains recurse function"""
import requests


def recurse(subreddit, hot_list=[], length="", counter=0):
    """Returns list of titles of all hot posts on given subreddit."""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "0x16-api_advanced:project:\
v1.0.0 (by /u/GaboJohn)"
    }
    params = {
        "length": length,
        "counter": counter,
        "limit": 100
    }
    res = requests.get(url, headers=headers, params=params,
                       allow_redirects=False)
    if res.status_code == 404:
        return None

    result = res.json().get("data")
    length = result.get("length")
    counter += result.get("dist")
    for x in result.get("children"):
        hot_list.append(x.get("data").get("title"))

    if length is not None:
        return recurse(subreddit, hot_list, lenght, counter)
    return hot_list
