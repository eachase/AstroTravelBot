import tweepy, time, sys
CONSUMER_KEY = ''#keep the quotes, replace this with your consumer key
CONSUMER_SECRET = ''#keep the quotes, replace this with your consumer secret key
ACCESS_KEY = ''#keep the quotes, replace this with your access token
ACCESS_SECRET = ''#keep the quotes, replace this with your access token secret
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
users = api.get_user('astrotravelbot')

friend_loc=[]
for friend in users.friends():
    location=friend.location.encode('ascii','ignore')
    friend_loc.append(location.rsplit(',',10)[0])


import csv
FoundYear = []
City = []
Region = []
Country = []
with open('City.csv','rb') as csvfile:
    lines = csv.reader(csvfile,delimiter=',')
    for line in lines:
        FoundYear.append((line[0]))
        City.append((line[1]))
        Region.append((line[2]))
        Country.append((line[3]))



for j in range(len(friend_loc)):
    for i in range(len(City)):
        if (friend_loc[j] == City[i]):
            print 'Did you know?',City[i],"was founded in the year",FoundYear[i],". Cool!"
        #if (friend_loc[j] !=City[i]) & (i == len(City)-1):
        #    print 'Your address is Earth, Solar System,Milky Way Galaxy, Local Group, Virgo Cluster, Universe'

    
    

