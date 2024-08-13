#!/usr/bin/python3
"""
get the total numbers of subcribers from the reddit api
subredit
"""
import requests


def number_of_subscribers(subreddit):
    """get the subreddit"""
    subRedditUrl = f'https://www.reddit.com/r/{subreddit}/about.json'

    redditGetUsrURL = requests.get(subRedditUrl, allow_redirects=False)

    try:
        if redditGetUsrURL.status_code == 200:

            subscriber = redditGetUsrURL.json()
            subNums = subscriber['data']['subscribers']
            return subNums
        elif redditGetUsrURL.status_code == 302:
            return 0
        else:
            return 0
    except Exception as e:
        print("An error occurred:", e)
