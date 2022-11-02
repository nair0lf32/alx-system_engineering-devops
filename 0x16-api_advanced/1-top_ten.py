#!/usr/bin/python3
"""Queries the Reddit API and prints the titles
of the first 10 hot posts for a given subreddit."""


def top_ten(subreddit):
    """function to query the Reddit API"""

    import requests

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'My User Agent 1.0'}
    try:
        response = requests.get(url, headers=headers,
                                allow_redirects=False)
        if response.status_code == 200:
            children = response.json().get('data').get('children')
            for i in range(10):
                print(children[i].get('data').get('title'))
        else:
            print("None")
    except Exception:
        print("None")
