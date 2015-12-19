# Python Reddit API Wrapper
import praw

def get_content(subreddit):
    """Fetch subreddit top month"""

    return {
        'title': 'Reddit /r/{} month top'.format(subreddit),
        'links': list(subreddit_links(subreddit))
    }

def subreddit_links(subreddit_name):
    r = praw.Reddit(user_agent='digester')
    subreddit = r.get_subreddit(subreddit_name)
    for s in subreddit.get_top_from_month():
        yield {'title' : s.title, 'url' : s.url}
    