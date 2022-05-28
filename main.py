import secrets
import tweepy
import time
import pandas

# read in keys
api_key = secrets.api_key
api_key_secret = secrets.api_key_secret
access_token = secrets.access_token
access_token_secret = secrets.access_token_secret

# authenticate
auth = tweepy.OAuth1UserHandler(
   api_key, api_key_secret, access_token, access_token_secret
)

api = tweepy.API(auth)

FILE_NAME = 'last_seen_id.txt'


def retrieve_last_seen_id(filename):
    f_read = open(filename, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id


def store_last_seen_id(last_seen_id, filename):
    f_write = open(filename, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return


last_seen_id = retrieve_last_seen_id(FILE_NAME)
mentions = api.mentions_timeline(since_id=last_seen_id)


for mention in reversed(mentions):
    last_seen_id = mention.id
    store_last_seen_id(last_seen_id, FILE_NAME)
    if '#followers' not in mention.text.lower():
        api.update_status(status=f'Hi, @{mention.user.screen_name}! May I help you? Check my bio for commands.',
                          in_reply_to_status_id=mention.id)
    if '#followers' in mention.text.lower():
        api.update_status(status=f'Hi, @{mention.user.screen_name}. I\'ll get back to you on that.',
                          in_reply_to_status_id=mention.id)
