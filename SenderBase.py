#-*- coding: utf-8 -*-

import os
import ast
import pytumblr
import facebook
from TwitterAPI import TwitterAPI

class BaseNetwork(object):
	""" Base class for social network APIs """
	
	def __init__(self, active, name):
		self.is_active = active
		self.network_name = name
		
	def post(self, message):
		"""
			Method posting a feedparser message to the implemented 
			social network.
			Returns True if successful
		"""
		pass


class SenderFacebook(BaseNetwork):
	""" Class implementing the Facebook API """

	def __init__(self, app_token, user_id, active):
		
		self.graph = facebook.GraphAPI(app_token)
		self.user_id = user_id
		
		BaseNetwork.__init__(self, active, 'Facebook')


	def post(self, message):
		
		title = message['title']
		link = message['link']
		
		try:
			#self.graph.put_object(self.user_id, "feed", message = title + '\n' + link)
			self.graph.put_wall_post(message = title, attachment = {'link':link}, profile_id = self.user_id)
		except Exception as e:
			print 'Facebook error : ', e.message
			return False
		
		return True


class SenderTumblr(BaseNetwork):
	""" Class implementing the Tumblr API """
	
	def __init__(self,consumer_key,consumer_secret,oauth_token,oauth_secret, active):
		
		self.client = pytumblr.TumblrRestClient(
			consumer_key,
			consumer_secret,
			oauth_token,
			oauth_secret,
		)
		
		BaseNetwork.__init__(self, active, 'Tumblr')		


	def post(self,message):
		
		info = self.client.info()
		if 'meta' in info:
			print 'Tumblr error : ' + info['meta']['msg']
			return
			
		blog_title = info['user']['name']
		
		title = message['title'].encode('utf8')
		body = message['summary_detail']['value'].encode('utf8') + "\n" + message['link'].encode('utf8')
		
		result = self.client.create_text(
			blog_title,
			state="published",
			title=title,
			body=body
		)
		
		if 'meta' in result:
			print 'Tumblr error : ' + result['response']['errors'][0]
		return ('id' in result)


class SenderTwitter(BaseNetwork):
	""" Class implementing the Twitter API """
	
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
		
		title = message['title']
		link = message['link']
	
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
	
		if len(r.text) < 500:
			result = ast.literal_eval(r.text)
			if 'errors' in result:
				print 'Twitter error : ' + result['errors'][0]['message']
				return False
		return True
	