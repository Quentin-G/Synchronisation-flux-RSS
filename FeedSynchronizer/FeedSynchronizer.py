import feedparser
import os
from time import mktime, sleep, time
from calendar import timegm
import ConfigParser
from threading import Timer
from SenderBase import SenderTumblr, SenderTwitter, SenderFacebook, SenderLinkedin

class FeedSynchronizer:
	""" Class synchronizing an RSS feed to social networks """
	
	def start(self):
		""" Starts the broadcast Timer """
		
		self.timestamp = time()
		self.timer = Timer(self.refresh_time, self._broadcast)
		self.timer.start()
		
	def stop(self):
		""" Stops the broadcast Timer """
		
		self.timer.cancel()
	
	def _broadcast(self):
		""" Fetches RSS entries to broadcast them on networks """
				
		if self.rss_url == '':
			print 'Error : RSS url missing'
			return
	
		parsed_rss = feedparser.parse(self.rss_url)
		if parsed_rss.bozo == 1:
			print 'Error : ' + parsed_rss.bozo_exception
			return
		if parsed_rss.entries == []:
			print 'Alert : no entries in this RSS feed'
			return
		
		# guid & date
		rss_guid = self.config.get('RSS', 'guid')
		if rss_guid == '':
			rss_guid = parsed_rss.entries[0].guid
			
		e = 0
		for entry in parsed_rss.entries:
			if rss_guid == entry.guid or self.timestamp >= timegm(entry.updated_parsed):
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

		self.timer = Timer(self.refresh_time, self._broadcast)
		self.timer.start()
			
	def set_refresh(self, refresh):
		""" Sets the refresh time """
		self.refresh_time = refresh
		self.config.set('RSS', 'refresh_time', refresh)
		self.config_save()
		
	def set_rss_url(self, url):
		"""  Sets the source RSS feed """
		self.config.set('RSS', 'url', url)
		self.rss_url = url
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
			self.config.set('RSS', 'refresh_time', 30)
			
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
			
			# config LinkedIn
			self.config.set('LinkedIn', 'active', False)
			self.config.set('LinkedIn', 'consumer_key', '')
			self.config.set('LinkedIn', 'consumer_secret', '')
			self.config.set('LinkedIn', 'user_token', '')
			self.config.set('LinkedIn', 'user_secret', '')
			
			# config save
			self.config_save()
		
		# Tumblr init
		active = self.config.getboolean('Tumblr', 'active')
		consumer_key = self.config.get('Tumblr', 'consumer_key')
		consumer_secret = self.config.get('Tumblr', 'consumer_secret')
		oauth_token = self.config.get('Tumblr', 'oauth_token')
		oauth_secret = self.config.get('Tumblr', 'oauth_secret')
		self.networkList.append(SenderTumblr(consumer_key, consumer_secret, oauth_token, oauth_secret, active))
		
		# Twitter init
		active = self.config.getboolean('Twitter', 'active')
		consumer_key = self.config.get('Twitter', 'consumer_key')
		consumer_secret = self.config.get('Twitter', 'consumer_secret')
		oauth_token = self.config.get('Twitter', 'oauth_token')
		oauth_secret = self.config.get('Twitter', 'oauth_secret')
		self.networkList.append(SenderTwitter(consumer_key, consumer_secret, oauth_token, oauth_secret, active))
		
		# Facebook init
		active = self.config.getboolean('Facebook', 'active')
		app_token = self.config.get('Facebook', 'app_token')
		user_id = self.config.get('Facebook', 'user_id')
		self.networkList.append(SenderFacebook(app_token, user_id, active))
		
		# LinkedIn init
		active = self.config.getboolean('LinkedIn', 'active')
		consumer_key = self.config.get('LinkedIn', 'consumer_key')
		consumer_secret = self.config.get('LinkedIn', 'consumer_secret')
		oauth_token = self.config.get('LinkedIn', 'user_token')
		oauth_secret = self.config.get('LinkedIn', 'user_secret')
		self.networkList.append(SenderLinkedin(consumer_key, consumer_secret, oauth_token, oauth_secret, active))
		
		self.rss_url = self.config.get('RSS', 'url')			
		self.refresh_time = self.config.getint('RSS', 'refresh_time')
			
			
			
			
			
			
			
			
