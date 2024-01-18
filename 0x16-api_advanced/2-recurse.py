#!/usr/bin/python3
"""
recursive function that queries the Reddit API and returns a
list containing the titles of all hot articles for a given subreddit
"""
import requests


def recurse(subreddit, hot_list=[]):
    """
    returns a list containing the titles of all hot articles
    for a given subreddit
    """
    if type(subreddit) is list:
        url = f"https://api.reddit.com/r/{subreddit[0]}?sort=hot&"
        url = f"{url}after={subreddit[1]}"
    else:
        url = f"https://api.reddit.com/r/{subreddit}?sort=hot"
        subreddit = [subreddit, ""]
    headers = {'User-Agent': 'Google Chrome Version 81.0.4044.129'}
    res = requests.get(url=url, headers=headers, allow_redirects=False)
    if res.status_code != 200:
        return (None)
    res = res.json()
    if "data" in res:
        data = res.get("data")
        if not data.get("children"):
            return (hot_list)
        for post in data.get("children"):
            hot_list += [post.get("data").get("title")]
        if not data.get("after"):
            return (hot_list)
        subreddit[1] = data.get("after")
        recurse(subreddit, hot_list)
        if hot_list[-1] is None:
            del hot_list[-1]
        return (hot_list)
    else:
        return (None)
