#!/usr/bin/python3
"""
Query the REDDIT API and find the
total number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers of reddit
    """
    url = f"https://api.reddit.com/r/{subreddit}/about"
    headers = {'User-Agent': 'Google Chrome Version 81.0.4044.129'}
    res = requests.get(url=url, headers=headers, allow_redirects=False)

    if res.status_code != 200:
        return 0
    res = res.json()
    if 'data' in res:
        return res.get('data').get('subscribers')
    else:
        return 0
