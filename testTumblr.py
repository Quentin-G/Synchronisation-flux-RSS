import pytumblr
import feedparser
import os
import time

# Authenticate via OAuth
client = pytumblr.TumblrRestClient(
	'1aAUvE8TDALhwVY92vc8mXzeiEOYTnPoc4af4zaNPoVL3g47J4',
	'C2ghgL6vVBQBgo0fCxd6PwsNso8TsMv9kih2kBWBdPBhVkYoKG',
	'NDzi0MlVj65EpME8qMhEJcsdWsIRDG4MuUXjqbp9a6U1iTY3tD',
	'xKHwdBdt5sBLqeKGSoGbr2EiF8MR0vZyMu5kAaf0TWflHubcVo'
)

while True:

	if os.path.exists('guid'):
		f = open('guid', 'r')
	else:
		f = open('guid', 'w')

	guid = f.read()
	f.close()

	# Getting RSS feed
	d = feedparser.parse('http://www.romandie.com/rss/flux.xml')

	# Counting the amount of new entries
	e = 0
	for entry in d.entries:
		if entry.guid == guid || guid != '':
			break
		e += 1

	post = False

	for i in range(e, 0, -1):
		title = d.entries[i-1].title.encode('utf8')
		body = d.entries[i-1].summary_detail.value.encode('utf8') + "\n" + d.entries[i-1].link.encode('utf8')
		client.create_text(
			"tagacoin", 
			state="published", 
			slug="testing-text-posts",
			title=title,
			body=body)
		post = True
		print('Message poste')


	if post:
		f = open('guid', 'w')
		f.write(d.entries[0].guid)
		f.close()
		
	time.sleep(30)

# d.entries[i].link
# d.entries[i].guid
