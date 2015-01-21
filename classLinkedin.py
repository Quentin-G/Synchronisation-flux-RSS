# -*- coding: utf-8 -*-
#Application µRSS enregistrée sur LikedIn
import feedparser
import os
import time
import sys
import linkedin


#USER_TOKEN= '36be6ec9-6875-4ab1-9329-197ab1b0be46'
#USER_SECRET= '75a83358-48e0-4f1c-a5eb-9b7a88771c6c'
#API_KEY= '78bqgh710g9l1x'
#API_SECRET= 'a2T3bYV0mwmX6zLj'

class RssLinkedin(BaseRss)

	def __init__(self,consumer_key,consumer_secret,oauth_token,oauth_secret):
		# Authenticate via OAuth
		self.authentication = linkedin.LinkedInDeveloperAuthentication(API_KEY, API_SECRET, USER_TOKEN, USER_SECRET, RETURN_URL, linkedin.PERMISSIONS.enums.values())
		self.application = linkedin.LinkedInApplication(authentication)

	def post(self,message):
		comment = ('Test de l\'API Python pour l\'envoi de contenu sur LinkedIn')
		title = message.title
		description = message.description
		link = message.link
		#Forme du message: ( Commentaire, titre, description, lien, image-url)  
		application.submit_share(comment, title, None, link, None )


