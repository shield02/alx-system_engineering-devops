#!/usr/bin/python3
"""
Queries the Reddit API and prints the titles of the
first 10 hot posts listed for a given subreddit
"""
import requests


def top_ten(subreddit):
    """
    prints titles of the first 10 hot posts
    """
    url = f"https://api.reddit.com/r/{subreddit}?sort=hot&limit=10"
    headers = {'User-Agent': 'Google Chrome Version 81.0.4044.129'}
    params = {'limit': 10}
    res = requests.get(url=url, headers=headers, params=params, allow_redirects=False)

    if res.status_code != 200:
        print(None)
        return
    result = res.json()
    try:
        data = result.get('data').get('children')
        for posts in data:
            print(posts.get('data').get('title'))
    except Exception:
        print(None)
