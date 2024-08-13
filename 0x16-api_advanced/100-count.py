"""gets hot topic with specific keywords"""
import requests
import re
from collections import defaultdict


def count_words(subreddit, word_list, after=None):
    """Query the Reddit API and count keyword occurrences in hot posts."""
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {
        'User-Agent': 'python:subreddit-word-count:v1.0 (by /u/yourusername)'}
    params = {'limit': 100}
    if after:
        params['after'] = after

    try:
        response = requests.get(url, headers=headers,
                                allow_redirects=False, params=params)

        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']
            word_counts = defaultdict(int)

            for post in posts:
                title = post['data']['title'].lower()
                for word in word_list:
                    count = len(re.findall(
                        r'\b' + re.escape(word.lower()) + r'\b', title))
                    word_counts[word.lower()] += count

            after = data['data'].get('after')
            if after:
                next_word_counts = count_words(subreddit, word_list, after)
                if next_word_counts:
                    for word, count in next_word_counts.items():
                        word_counts[word] += count

            sorted_counts = sorted(word_counts.items(),
                                   key=lambda x: (-x[1], x[0]))
            for word, count in sorted_counts:
                if count > 0:
                    print(f"{word}: {count}")
        elif response.status_code == 302:
            print(None)
        else:
            print(None)
    except Exception:
        print(None)
