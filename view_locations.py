import tweepy, time, sys

CONSUMER_KEY = ' '#keep the quotes, replace this with your consumer key
CONSUMER_SECRET = ' '#keep the quotes, replace this with your consumer secret key
ACCESS_KEY = ' '#keep the quotes, replace this with your access token
ACCESS_SECRET = ' '#keep the quotes, replace this with your access token secret
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

import pyowm  
owm = pyowm.OWM('ec4c93234544d284adf07e0e4e89660e')

#import twitter
#users = api.get_user('mjn693')
users = api.get_user('astrotravelbot')

#for friend in users.friends():
#    print friend.location


for friend in users.followers():
   print(friend.location)
   try:
       observation = owm.weather_at_place(friend.location)  
       w = observation.get_weather()  
       print(w.get_wind()) # see attribute list for different weather info.
   except:
       print("no location found")
