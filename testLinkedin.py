# -*- coding: utf-8 -*-

#Application µRSS enregistrée sur LikedIn
import feedparser
import os
import time
import sys
sys.path.append('/usr/local/lib/python2.7/dist-packages/')
from linkedin import linkedin

# Token utilisateur: 	36be6ec9-6875-4ab1-9329-197ab1b0be46
# Secret utilisateur: 	75a83358-48e0-4f1c-a5eb-9b7a88771c6c

# clé API: 		78bqgh710g9l1x
# Clé secrète: 	a2T3bYV0mwmX6zLj

USER_TOKEN= '36be6ec9-6875-4ab1-9329-197ab1b0be46'
USER_SECRET= '75a83358-48e0-4f1c-a5eb-9b7a88771c6c'

RETURN_URL = "https://www.tumblr.com/"

API_KEY= '78bqgh710g9l1x'
API_SECRET= 'a2T3bYV0mwmX6zLj'

#Authentification pour accéder à son propre contenu: pas besoin de configurer OAuth 2.0
authentication = linkedin.LinkedInDeveloperAuthentication(API_KEY, API_SECRET, USER_TOKEN, USER_SECRET, RETURN_URL, linkedin.PERMISSIONS.enums.values())

application = linkedin.LinkedInApplication(authentication)

# Getting RSS feed
d = feedparser.parse('http://jsuis-un-canard.tumblr.com/rss')
comment = ('Test de l\'API Python pour l\'envoi de contenu sur LinkedIn')
title = d.entries[1].title
description = d.entries[1].description
link = d.entries[1].link

#Forme du message: ( Commentaire , titre, description, lien, image-url )  
application.submit_share(comment, title, None, link, None )


