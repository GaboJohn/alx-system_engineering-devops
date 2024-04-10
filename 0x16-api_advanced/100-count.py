#!/usr/bin/python3
""" Module for a function that queries the
    Reddit Api recursively """

import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """
    Recursively queries the Reddit API, parses hot article titles,
    counts occurrences of given keywords, and prints results sorted.

    Args:
        subreddit (str): The name of the subreddit to retrieve hot
        articles from.
        word_list (list): A list of keywords to count occurrences for.
        after (str): A token indicating the start of the next page of
        results (default None).
        counts (dict): A dictionary to store keyword counts (default None).

    Returns:
        None
    """
    if counts is None:
        counts = {}

    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {'User-Agent': 'MyScript/1.0'}

    params = {'limit': 100}  # Number of posts per page (maximum is 100)

    if after:
        params['after'] = after

    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)
        response.raise_for_status()

        data = response.json()
        posts = data['data']['children']

        # Process each post title
        for post in posts:
            title = post['data']['title']
            process_title(title, word_list, counts)

        # Recursively call count_words function for next page if exists
        after = data['data'].get('after')
        if after:
            count_words(subreddit, word_list, after, counts)

    except requests.RequestException:
        return

    # Print sorted counts at the end of recursion
    print_sorted_counts(counts)


def process_title(title, word_list, counts):
    """
    Process a title to count occurrences of keywords in the word_list.

    Args:
        title (str): The title of a Reddit post.
        word_list (list): A list of keywords to count occurrences for.
        counts (dict): A dictionary to store keyword counts.

    Returns:
        None
    """
    words = title.lower().split()  # Split title into lowercase words

    for word in words:
        # Clean word by removing punctuation
        cleaned_word = word.strip('.,!?_')

        if cleaned_word in word_list:
            if cleaned_word in counts:
                counts[cleaned_word] += 1
            else:
                counts[cleaned_word] = 1


def print_sorted_counts(counts):
    """
    Print sorted keyword counts in descending order by count,
    and alphabetically by keyword if counts are the same.

    Args:
        counts (dict): A dictionary containing keyword counts.

    Returns:
        None
    """
    sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))

    for keyword, count in sorted_counts:
        print(f"{keyword}: {count}")
