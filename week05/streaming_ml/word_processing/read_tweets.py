import twitter
import time
import json
import dateutil.parser
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

consumer_key = os.environ['TWITTER_CONSUMER_KEY']
consumer_secret = os.environ['TWITTER_CONSUMER_SECRET']
access_token = os.environ['TWITTER_ACCESS_TOKEN']
access_secret = os.environ['TWITTER_ACCESS_TOKEN_SECRET']

auth = twitter.OAuth(token=access_token, token_secret=access_secret, 
consumer_key=consumer_key, consumer_secret=consumer_secret)

twitter_stream = twitter.TwitterStream(auth=auth)


class Tweet(dict):
    def __init__(self, tweet_in, encoding  = 'utf-8'):
        super(Tweet, self).__init__(self)
        if tweet_in and 'delete' not in tweet_in:
            self['id']           = tweet_in['id']
            self['geo']          = tweet_in['geo']['coordinates'] if tweet_in['geo'] else None
            self['text']         = tweet_in['text'].encode(encoding)
            self['user_id']      = tweet_in['user']['id'] 
            self['hashtags']     = [x['text'].encode(encoding) \
                                   for x in tweet_in['entities']['hashtags']]
            self['timestamp']    = dateutil.parser \
.parse(tweet_in[u'created_at']).replace(tzinfo=None).isoformat()
            self['screen_name']  = tweet_in['user']['screen_name'] \
.encode(encoding)

def get_next_tweet(twitter_stream):
    block = False
    stream = twitter_stream.statuses.sample(block=False)
    tweet_in = None
    
    while not tweet_in or 'delete' in tweet_in:
        tweet_in = stream.next()
        tweet_parsed = Tweet(tweet_in)
        
    return json.dumps(tweet_parsed)
