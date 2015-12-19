# Python reddit API wrapper
import praw

"""Return month top for subreddit or all"""
def monthly(config):
    r = praw.Reddit(user_agent='digester')
    submissions_list = []
    for subreddit in config['subreddits']:
        submissions = []
        if subreddit:
            sub = r.get_subreddit(subreddit)
            submissions = [s for s in sub.get_top_from_month()]
        else:
            submissions = [s for s in r.get_top({'sort':'top', 't':'month'})]

        d = {'name': subreddit, 'links': [{'title' : s.title, 'url' : s.url} for s in submissions]}
        submissions_list.append(d)
    
    return submissions_list
