import secrets
import tweepy
import time
import pandas

api_key = secrets.api_key
api_key_secret = secrets.api_key_secret
acces_token = secrets.access_token
access_token_secret = secrets.access_token_secret

auth = tweepy.OAuth1UserHandler(
   api_key, api_key_secret, access_token, access_token_secret
)

api = tweepy.API(auth)

