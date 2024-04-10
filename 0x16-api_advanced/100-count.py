#!/usr/bin/python3
""" Module for a function that queries the Reddit API recursively."""

import requests


def count_words(subreddit, word_list, after=None, counts=None):
    if not subreddit or not word_list:
        return

    if counts is None:
        counts = {}

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "MyScript/1.0"}

    params = {"limit": 100}
    if after:
        params["after"] = after

    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)
        response.raise_for_status()

        data = response.json()
        children = data["data"]["children"]

        for post in children:
            title = post["data"]["title"].lower()
            for word in word_list:
                if word.lower() in title:
                    counts[word.lower()] = counts.get(word.lower(), 0) +
                    title.count(word.lower())

        after = data["data"]["after"]
        if after:
            count_words(subreddit, word_list, after, counts)

    except (requests.RequestException, KeyError) as e:
        print(f"Error processing subreddit '{subreddit}': {e}")

    if counts:
        sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_counts:
            print(f"{word}: {count}")
