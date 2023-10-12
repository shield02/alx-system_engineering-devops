#!/usr/bin/python3
"""
A function to Query Reddit API
"""
import requests


def top_ten(subreddit):
    """
        Print top 10 titles for a given subreddit or None
    """
    headers = requests.utils.default_headers()
    headers.update({'User-Agent': 'My User Agent 1.0'})

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    r = requests.get(url, headers=headers).json()
    top_ten = r.get('data', {}).get('children', [])
    if not top_ten:
        print(None)
    for title in top_ten:
        print(title.get('data').get('title'))
