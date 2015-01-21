import pytumblr
import feedparser
import os
from time import mktime, sleep, time
import ConfigParser

from RssBase import RssTumblr, RssTwitter, RssFacebook

class FeedSynchronizer:
	""" Class synchronizing an RSS feed to social networks """
	
	def run(self):
		""" Main method, fetching RSS entries to post them """
		
		# tmp
		rss_date = 0
		
		rss_url = self.config.get('RSS', 'url')
		if rss_url == '':
			print 'Error : RSS url missing'
			return		
		
		# main loop
		while True:
			parsed_rss = feedparser.parse(rss_url)
			if parsed_rss.bozo == 1:
				print 'Error : ' + parsed_rss.bozo_exception
				return
			if parsed_rss.entries == []:
				print 'Alert : no entries in this RSS feed'
				
			# waiting for entries
			while parsed_rss.entries == []:
				sleep(30)
				parsed_rss = feedparser.parse(rss_url)
			
			# guid & date
			rss_guid = self.config.get('RSS', 'guid')
			if rss_guid == '':
				rss_guid = parsed_rss.entries[0].guid
			#rss_date = self.config.getfloat('RSS', 'date')
			#if rss_date == 0:
			#	rss_date = mktime(parsed_rss.entries[0].published_parsed)
				
			e = 0
			for entry in parsed_rss.entries:
				if rss_guid == entry.guid or rss_date >= mktime(entry.updated_parsed):
					break
				e+=1
				
			# posting
			for i in range(e, 0, -1):
				for network in self.networkList:
					if network.is_active:
						if network.post(parsed_rss.entries[i - 1]):
							print 'Message posted on ' + network.network_name
						else:
							print 'Message not posted on ' + network.network_name
			
			self.config.set('RSS', 'guid', parsed_rss.entries[0].guid)
			#self.config.set('RSS', 'date', mktime(parsed_rss.entries[0].published_parsed))
			self.config_save()
			
			sleep(30)
		
	def set_rss_url(self, url):
		"""  Method to set the source RSS feed """
		self.config.set('RSS', 'url', url)
		self.config.set('RSS', 'guid', '')
		self.config.set('RSS', 'date', 0.0)
		self.config_save()
	
	def set_network_active(self, network_name, is_active):
		""" Method to activate/deactivate the use of a network """
		
		if self.config.has_option(network_name, 'active'):
			self.config.set(network_name, 'active', is_active)			
			self.config_save()
			
			for network in self.networkList:
				if network.network_name == network_name:
					network.is_active = is_active
					break
		else:
			print 'Error : "' + network_name + '" does not exist'
			return
	
	def init_tumblr(self, consumer_key, consumer_secret, oauth_token, oauth_secret, active=False):
		""" method to initialize the Tumblr API """
		
		self.config.set('Tumblr', 'consumer_key', consumer_key)
		self.config.set('Tumblr', 'consumer_secret', consumer_secret)
		self.config.set('Tumblr', 'oauth_token', oauth_token)
		self.config.set('Tumblr', 'oauth_secret', oauth_secret)
		self.config.set('Tumblr', 'active', active)
		set_network_active('Tumblr', active)
		self.config_save()
			
	def init_twitter(self, consumer_key, consumer_secret, oauth_token, oauth_secret, active=False):
		""" method to initialize the Twitter API """
		
		self.config.set('Twitter', 'consumer_key', consumer_key)
		self.config.set('Twitter', 'consumer_secret', consumer_secret)
		self.config.set('Twitter', 'oauth_token', oauth_token)
		self.config.set('Twitter', 'oauth_secret', oauth_secret)
		self.config.set('Twitter', 'active', active)
		set_network_active('Twitter', active)
		self.config_save()
				
	def init_facebook(self, app_token, user_id, active=False):
		""" method to initialize the Facebook API """
		
		self.config.set('Facebook', 'active', active)
		self.config.set('Facebook', 'app_token', app_token)
		self.config.set('Facebook', 'user_id', user_id)
		set_network_active('Facebook', active)
		self.config_save()
		
	def config_save(self):
		""" Method to save the current config in a file """
		with open('config.cfg', 'wb') as configfile:
				self.config.write(configfile)
				
	def __init__(self):
		""" Initialization of the config file and network list """
		self.config = ConfigParser.RawConfigParser()
		self.networkList = []
		
		# first execution
		if self.config.read('config.cfg') == []:
			
			# config sections
			self.config.add_section('RSS')
			self.config.add_section('Tumblr')
			self.config.add_section('Twitter')
			self.config.add_section('Facebook')
			
			# config RSS
			self.config.set('RSS', 'url', '')
			self.config.set('RSS', 'guid', '')
			self.config.set('RSS', 'date', 0.0)
			
			# config Tumblr
			self.config.set('Tumblr', 'active', False)
			self.config.set('Tumblr', 'consumer_key', '')
			self.config.set('Tumblr', 'consumer_secret', '')
			self.config.set('Tumblr', 'oauth_token', '')
			self.config.set('Tumblr', 'oauth_secret', '')
			
			# config Twitter
			self.config.set('Twitter', 'active', False)
			self.config.set('Twitter', 'consumer_key', '')
			self.config.set('Twitter', 'consumer_secret', '')
			self.config.set('Twitter', 'oauth_token', '')
			self.config.set('Twitter', 'oauth_secret', '')
			
			# config Facebook
			self.config.set('Facebook', 'active', False)
			self.config.set('Facebook', 'app_token', '')
			self.config.set('Facebook', 'user_id', '')
			
			# config save
			self.config_save()
		
		# Tumblr init
		tumblr_active = self.config.getboolean('Tumblr', 'active')
		consumer_key = self.config.get('Tumblr', 'consumer_key')
		consumer_secret = self.config.get('Tumblr', 'consumer_secret')
		oauth_token = self.config.get('Tumblr', 'oauth_token')
		oauth_secret = self.config.get('Tumblr', 'oauth_secret')
		self.networkList.append(RssTumblr(consumer_key, consumer_secret, oauth_token, oauth_secret, tumblr_active))
		
		# Twitter init
		twitter_active = self.config.getboolean('Twitter', 'active')
		consumer_key = self.config.get('Twitter', 'consumer_key')
		consumer_secret = self.config.get('Twitter', 'consumer_secret')
		oauth_token = self.config.get('Twitter', 'oauth_token')
		oauth_secret = self.config.get('Twitter', 'oauth_secret')
		self.networkList.append(RssTwitter(consumer_key, consumer_secret, oauth_token, oauth_secret, twitter_active))
		
		# Facebook init
		facebook_active = self.config.getboolean('Facebook', 'active')
		app_token = self.config.get('Facebook', 'app_token')
		user_id = self.config.get('Facebook', 'user_id')
		self.networkList.append(RssFacebook(app_token, user_id, facebook_active))
				
		
			
			
			
			
			
			
			
			
			