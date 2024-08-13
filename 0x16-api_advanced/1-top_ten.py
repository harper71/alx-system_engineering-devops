#!/usr/bin/python3
"""
get the fist 10
hot topics in the api
"""
import requests


def top_ten(subreddit):
    """get the top 10"""
    hotTopicUrl = f'https://www.reddit.com/r/{subreddit}/hot.json'

    response = requests.get(hotTopicUrl, allow_redirects=False,
                            params={'limit': 10})

    if response.status_code == 200:
        data = response.json()
        totalPost = data['data']['children']

        if not totalPost:
            print(None)
            return

        for posts in totalPost:
            top10Posts = posts['data']['title']
            print(f"{top10Posts}")
    elif response.status_code == 302:
        print(None)
    else:
        print(None)
