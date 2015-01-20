import feedparser
import os
import time
import sys
sys.path.append('/usr/local/lib/python2.7/dist-packages/')
from TwitterAPI import TwitterAPI

# Authenticate via OAuth
#consumer_key = "YhHSnELMJFPyiHYDL8EgfSAwg" 
#consumer_secret = "MaJswpbog1XeuNr71WqxLnxM7njoBlZRKX6s5g90oWphug2NGM"
#access_token_key = "2912679658-iQxKsmTjJBSquQm66zExG7RvFxJKi3Z8mCwh4gY"
#access_token_secret = "S5CZAtOfZrDL4RXqve2qR9azRaYkD5Ng3OygZlWzK4xEq"

class RssTwitter(BaseRss):

	def __init__(self,consumer_key,consumer_secret,oauth_token,oauth_secret):
		self.client = TwitterAPI(
			consumer_key,
			consumer_secret,
			access_token_key,
			access_token_secret
		)


	def post(self,message)
		title = message.title
		link = message.link
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
	

