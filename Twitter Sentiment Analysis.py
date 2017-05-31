# 1. sign up to access twitter apis at dev.twitter.com
# 2. create a dummy application and generate access token
# 3. install textblob e.g pip install textblob
# 4. install tweepy e.g. pip install tweepy
import tweepy
from textblob import TextBlob
consumer_key = 'N8lpQXJgVKnxpLC9vOKh5NyWm'
consumer_secret = 'AntyEPNglrosKejH09v7qn5DgqtXwfzFGQNOshHXtA3gtiyop2'

access_token =  '3325621526-kVGiBn45yaCtGAFjxnVgYcwRpJTNuuFVMBtI5Qi'
access_token_secret = 'oW4BF7yZNOSKU6OSUqQbvyYU0zomzoswhByPDW0kUyzUA'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
public_tweets = api.search('Trump')
for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
