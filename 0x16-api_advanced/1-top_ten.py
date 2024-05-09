#!/usr/bin/python3
""" Script to get the first 10 hot
    posts on Reddit
"""
from requests import get


def top_ten(subreddit):
    """
    Get the first 10 hot posts for a subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        None

    Prints the titles of the first 10 hot posts for the given subreddit.
    If the subreddit is invalid or the request fails, it prints None.
    """
    if subreddit and type(subreddit) is str:
        url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
        headers = {'user-agent': 'my-app/0.0.1'}
        params = {'limit': 10}
        req = get(url, params=params, headers=headers, allow_redirects=False)
        if req.status_code == 200:
            data = req.json()
            posts = data.get('data', {}).get('children', {})
            for post in posts:
                print(post.get('data').get('title'))
        else:
            print(None)
