#!/usr/bin/python3
"""
Query the REDDIT API and find
the total number of sibscribers
"""
import requests


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers of reddit
    """
    if subreddit is None or not isinstance(subreddit, str):
        return (0)

    url = f'https://api.reddit.com/r/{subreddit}/about'
    headers = {'user-agent': 'Google Chrome Version 81.0.4044.129'}
    res = requests.get(url=url, headers=headers, allow_redirects=False)
    result = res.json()

    try:
        return result.get('data').get('subscribers')
    except Exception:
        return (0)
