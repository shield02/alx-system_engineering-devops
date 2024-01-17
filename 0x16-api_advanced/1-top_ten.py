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
    res = requests.get(url=url, headers=headers, allow_redirects=False)

    if res.status_code != 200:
        print(None)
        return
    res = res.json()
    if 'data' in res:
        for posts in res.get('data').get('children'):
            print(posts.get('data').get('title'))
    else:
        print(None)
