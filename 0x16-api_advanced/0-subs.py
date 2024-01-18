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
    if subreddit is None or not isinstance(subreddit, str):
        return(0)

    url = "https://api.reddit.com/r/{}/about".format(subreddit)
    headers = {'User-Agent': 'Google Chrome Version 81.0.4044.129'}
    res = requests.get(url, headers=headers)
    result = res.json()

    try:
        return result.get('data').get('subscribers')
    except Exception:
        return(0)
