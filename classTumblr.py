import pytumblr
import os


#	consumer_key	'1aAUvE8TDALhwVY92vc8mXzeiEOYTnPoc4af4zaNPoVL3g47J4',
#	consumer_secret	'C2ghgL6vVBQBgo0fCxd6PwsNso8TsMv9kih2kBWBdPBhVkYoKG',
#	oauth_token		'NDzi0MlVj65EpME8qMhEJcsdWsIRDG4MuUXjqbp9a6U1iTY3tD',
#	oauth_secret	'xKHwdBdt5sBLqeKGSoGbr2EiF8MR0vZyMu5kAaf0TWflHubcVo'

class RssTumblr(BaseRss):


	def __init__(self,consumer_key,consumer_secret,oauth_token,oauth_secret):
		# Authenticate via OAuth
		self.client=pyTumblr.TumblrRestClient(
			consumer_key,
			consumer_secret,
			oauth_token,
			oauth_secret,
		)
				


	def post(self,message):
		title =message.title.encode('utf8')
		body = message.summary_detail.value.encode('utf8') + "\n" + message.link.encode('utf8')
		client.create_text(
			message["user"]["name"], 
			state="published", 
			slug="testing-text-posts",
			title=title,
			body=body)

	
