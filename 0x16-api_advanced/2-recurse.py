#!/usr/bin/python3
"""
get all
hot topics in the api
"""
import requests


def recurse(subreddit, hot_list=[]):
    """get all hot"""

    hotTopicUrl = f'https://www.reddit.com/r/{subreddit}/hot.json'

    limit = {'limit': 100}
    if hot_list:
        limit['hot_list'] = hot_list

    try:
        response = requests.get(hotTopicUrl, allow_redirects=False,
                                params=limit)
        if response.status_code == 200:
            data = response.json()
            totalPost = data['data']['children']

            if not totalPost:
                return None

            allHotPosts = [post['data']['title'] for post in totalPost]
            hot_list = data['data'].get('hot_list')

            if hot_list:
                more_hotPosts = recurse(subreddit, hot_list)
                if more_hotPosts:
                    allHotPosts.extend(more_hotPosts)

            return(allHotPosts)
        elif response.status_code == 302:
            return None
        else:
            return None
    except Exception as e:
        print("an error occured:", e)
