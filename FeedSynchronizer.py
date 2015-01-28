import pytumblr
import feedparser
import os
from time import mktime, sleep, time
from calendar import timegm
import ConfigParser

from SenderBase import SenderTumblr, SenderTwitter, SenderFacebook

class FeedSynchronizer:
	""" Class synchronizing an RSS feed to social networks """
	
	def run(self):
		""" Fetches RSS entries to broadcast them on networks """
		
		timestamp = time()
		
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
				
			e = 0
			for entry in parsed_rss.entries:
				if rss_guid == entry.guid or timestamp >= timegm(entry.updated_parsed):
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
			self.config_save()
			
			sleep(30)
		
	def set_rss_url(self, url):
		"""  Sets the source RSS feed """
		self.config.set('RSS', 'url', url)
		self.config.set('RSS', 'guid', '')
		self.config_save()
	
	def set_network_active(self, network_name, is_active):
		""" Activates/deactivates the use of a network """
		
		if not self.config.has_option(network_name, 'active'):
			print 'Error : "' + network_name + '" does not exist'
			return
		
		self.config.set(network_name, 'active', is_active)			
		self.config_save()
		
		for network in self.networkList:
			if network.network_name == network_name:
				network.is_active = is_active
				break
			
	
	def init_network(self, network_name, keys_dict, active=False):
		""" Initializes an existing social network API """
		
		if not self.config.has_section(network_name):
			print 'Error : "' + network_name + '" does not exist'
			return
		
		for key in keys_dict:
			if not self.config.has_option(network_name, key):
				print 'Error : "' + key + '" does not exist in "' + network_name + '"'
				return
			self.config.set(network_name, key, keys_dict[key])
			
		self.config.set(network_name, 'active', active)
		self.set_network_active(network_name, active)
		self.config_save()
		
		
	def config_save(self):
		""" Saves the current config in a file """
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
		self.networkList.append(SenderTumblr(consumer_key, consumer_secret, oauth_token, oauth_secret, tumblr_active))
		
		# Twitter init
		twitter_active = self.config.getboolean('Twitter', 'active')
		consumer_key = self.config.get('Twitter', 'consumer_key')
		consumer_secret = self.config.get('Twitter', 'consumer_secret')
		oauth_token = self.config.get('Twitter', 'oauth_token')
		oauth_secret = self.config.get('Twitter', 'oauth_secret')
		self.networkList.append(SenderTwitter(consumer_key, consumer_secret, oauth_token, oauth_secret, twitter_active))
		
		# Facebook init
		facebook_active = self.config.getboolean('Facebook', 'active')
		app_token = self.config.get('Facebook', 'app_token')
		user_id = self.config.get('Facebook', 'user_id')
		self.networkList.append(SenderFacebook(app_token, user_id, facebook_active))
				
		
			
			
			
			
			
			
			
			
			