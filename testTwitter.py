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

client = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)

while True:

	if os.path.exists('guid'):
		f = open('guid', 'r')
	else:
		f = open('guid', 'w')

	guid = f.read()
	f.close()

	# Getting RSS feed
	d = feedparser.parse('http://jsuis-un-canard.tumblr.com/rss')

	# Counting the amount of new entries
	e = 0
	for entry in d.entries:
		if entry.guid == guid or guid != '':
			break
		e += 1

	post = False

	for i in range(e, 0, -1):
		title = d.entries[i-1].title.encode('utf8')
		r = api.request('statuses/update', {'status':body.title.encode('utf8')})
		post = True
		print('Message poste')


	if post:
		f = open('guid', 'w')
		f.write(d.entries[0].guid)
		f.close()
		
	time.sleep(30)

# d.entries[i].link
# d.entries[i].guid

	



r = api.request('statuses/update', {'status':body.title.encode('utf8')})
print r.status_code
