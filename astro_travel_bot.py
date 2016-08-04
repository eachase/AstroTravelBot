from __future__ import division
import tweepy



if __name__ == '__main__':
	# Check if you were followed

	# Get location of recent follower

	# Tweet something related to the location at this recent follower

	key_file = open("access_codes.txt", "r")
	keys = []
	for line in key_file:
		keys.append(line.strip()) 	

	consumer_key = keys[0]
	consumer_secret = keys[1]
	access_token = keys[2]
	access_token_secret = keys[3]

	
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)

	api = tweepy.API(auth)

	public_tweets = api.home_timeline()
	for tweet in public_tweets:
	    print tweet.text
	

	key_file.close()


