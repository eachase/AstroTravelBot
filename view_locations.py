import tweepy, time, sys

CONSUMER_KEY = ' '#keep the quotes, replace this with your consumer key
CONSUMER_SECRET = ' '#keep the quotes, replace this with your consumer secret key
ACCESS_KEY = ' '#keep the quotes, replace this with your access token
ACCESS_SECRET = ' '#keep the quotes, replace this with your access token secret
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

#import twitter
#users = api.get_user('mjn693')
users = api.get_user('astrotravelbot')
for friend in users.friends():
    print friend.location
