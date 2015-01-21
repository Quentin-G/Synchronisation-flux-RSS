#-*- coding: utf-8 -*-

import os
import ast
import pytumblr
import facebook
from TwitterAPI import TwitterAPI

class BaseNetwork(object):
	
	def __init__(self, active, name):
		self.is_active = active
		self.network_name = name
		
	def post(self, message):
		pass


class RssFacebook(BaseNetwork):

	def __init__(self, app_token, user_id, active):
		self.graph = facebook.GraphAPI(app_token)
		self.app_token = app_token
		self.user_id = user_id
		BaseNetwork.__init__(self, active, 'Facebook')

	def post(self, message):
		title = message['title']
		link = message['link']
		try:
			self.graph.put_object(self.user_id, "feed", message = title + '\n' + link)
		except:
			return False
		
		return True # todo


class RssTumblr(BaseNetwork):

	def __init__(self,consumer_key,consumer_secret,oauth_token,oauth_secret, active):
		self.client = pytumblr.TumblrRestClient(
			consumer_key,
			consumer_secret,
			oauth_token,
			oauth_secret,
		)
		self.blog_title = self.client.info()['user']['name']
		BaseNetwork.__init__(self, active, 'Tumblr')		


	def post(self,message):
		title = message.title.encode('utf8')
		body = message.summary_detail.value.encode('utf8') + "\n" + message.link.encode('utf8')
		
		result = self.client.create_text(
			self.blog_title,
			state="published",
			title=title,
			body=body
		)
		
		return ('id' in result)


class RssTwitter(BaseNetwork):

	def __init__(self, consumer_key, consumer_secret, oauth_token, oauth_secret, active):
		self.consumer_key = consumer_key
		self.consumer_secret = consumer_secret
		self.oauth_token = oauth_token
		self.oauth_secret = oauth_secret
		
		BaseNetwork.__init__(self, active, 'Twitter')

	def post(self, message):
		api = TwitterAPI(
			self.consumer_key,
			self.consumer_secret,
			self.oauth_token,
			self.oauth_secret
		)
		
		title = message.title
		link = message.link
		
		if(len(title) > 114):
			words = title.split(" ")
			i = 1
			statut = words[0]
			while len(statut) + len(words[i]) < 114 :
				statut += ' ' + words[i]
				i+=1
			r = api.request('statuses/update', {'status':statut + '... ' + link})
		else:
			r = api.request('statuses/update', {'status':title + ' ' + link})
		
		result = ast.literal_eval(r.text)
		if 'errors' in r.text:
			# print 'Twitter error : ' + result['errors'][0]['message']
			return False
		return True
	