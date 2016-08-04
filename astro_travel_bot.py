from __future__ import division
import tweepy



if __name__ == '__main__':
	# Check if you were followed

	# Get location of recent follower

	# Tweet something related to the location at this recent follower

	#
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)

	api = tweepy.API(auth)

	public_tweets = api.home_timeline()
	for tweet in public_tweets:
	    print tweet.text


