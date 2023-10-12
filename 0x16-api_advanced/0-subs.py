#!/usr/bin/python3
"""
A function to Query Reddit API
"""
import requests


def number_of_subscribers(subreddit):
    """
        Query Reddit API
        return number of subscribers for a given subreddit or 0
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    headers = requests.utils.default_headers()
    headers.update({'User-Agent': 'My User Agent 1.0'})

    r = requests.get(url, headers=headers).json()
    subscribers = r.get('data', {}).get('subscribers')
    if not subscribers:
        return 0
    return subscribers
