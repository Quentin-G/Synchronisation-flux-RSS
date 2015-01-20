import feedparser
import os
import time
import sys
sys.path.append('/usr/local/lib/python2.7/dist-packages/')
import facebook

#token = '601341816634019|1ds__S2_N7gIig2THoHa1mK4NiI'	#APP_TOKEN µRSS
#profile = graph.get_object('1214687540')				#ID_USER Quentin Girod

class RssFacebook(BaseRss):

	# __init__ différent : 2 paramètres
	def __init__(self,APP_TOKEN,ID_USER):
		graph = facebook.GraphAPI(APP_TOKEN)
		self.APP_TOKEN=APP_TOKEN


	def post(self,message):	#Caution: encoding utf8 needed
		title = message.title
		link = message.link

		graph.put_object(APP_TOKEN, "feed", message= title+'\n'+link)
