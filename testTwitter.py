import feedparser
import os
import time
import sys
sys.path.append('/usr/local/lib/python2.7/dist-packages/')
from TwitterAPI import TwitterAPI

# Authenticate via OAuth
consumer_key = "YhHSnELMJFPyiHYDL8EgfSAwg" 
consumer_secret = "MaJswpbog1XeuNr71WqxLnxM7njoBlZRKX6s5g90oWphug2NGM"
access_token_key = "2912679658-iQxKsmTjJBSquQm66zExG7RvFxJKi3Z8mCwh4gY"
access_token_secret = "S5CZAtOfZrDL4RXqve2qR9azRaYkD5Ng3OygZlWzK4xEq"

api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)

# Getting RSS feed
d = feedparser.parse('http://jsuis-un-canard.tumblr.com/rss')

# Counting the amount of new entries
e = 0

post = False

title = d.entries[0].title
link = d.entries[0].link
print(title)
if(len(title)>114):
	words = title.split(" ")
	i = 1
	statut= words[0]
	while len(statut)+len(words[i])<114 :
		statut+=' '+words[i]
		i+=1
	r = api.request('statuses/update', {'status':statut+'... '+link})
else:
	r = api.request('statuses/update', {'status':title+' '+link})
	

post = True
print('Message poste :')
print(r.text)


# d.entries[i].link
# d.entries[i].guid

