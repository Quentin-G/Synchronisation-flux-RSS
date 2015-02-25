Synchronisation-flux-RSS
========================

**Projet de Master 1 informatique.**

#Needs

You just need [Python](https://www.python.org/downloads/) to execute the files

#Get ready
* [The main app](#the-main-app)
* [set up with facebok](#set-up-with-facebook)
* [set up with twitter](#set-up-with-twitter)
* [Set up with LinkedIn](#set-up-with-linkedin)
* [Set un with Tumblr](#set-up-with-tumblr)


#The main app
Fisrt of all, you need to download the 2 files : "FeedSynchronizer.py" and "SenderBase.py".
You have to modify FeedSynchronizer.py in order to choose an RSS flux to follow (line 134).

    # config RSS
    self.config.set('RSS', 'url', 'YOUR_RSS_URL_HERE')

You may also modify the following lines to configure social networks with this RSS. Learn how to do it with the following parts of this manual.

Once the modifications are done, execute FeedSynchronizer.py. You get a "config.cfg" file used by FeedSynchronizer. If you delete it, a new execution will create a new one.
FeedSynchronizer now endlessly check the RSS flux and post new instances on the configured social networks.

To end the execution, use the "stop" method on the instancied variable.

#Set up with Facebook 

You have the solution to just [set up twitter](#set-up-with-twitter) and then link your facebook account.

Otherwise...
You need :
* facebook-sdk API for python 
* Register your own App on facebook
* Find the necessary IDs
* Grant the rights for App to publish


###facebook-sdk
Get it on [GitHub](https://github.com/pythonforfacebook/facebook-sdk).

###Register your Facebook App
To create your application, go to [developpers facebook](https://developers.facebook.com/), 
register yourself as a developper (valid phone  umber needed), then on "My Apps", select 
"Add a new App".

###Get the IDs
You'll need the **ACCESS_TOKEN** which is at: 
"Tool & Support -> Access Token Debugger". The **ACCESS_TOKEN** looks like:

APP ID|1ds__S2_N7gIig2THoHxxxxxxxx

You'll also need your**ID_USER**. Go to https://graph.facebook.com/firstname.lastname
the first information: "id" is the'**ID_USER** you need.

###Grant publishing right
The Facebook account has to allow the facebook application to publish by its name. In order to do it, follow [this link](https://developers.facebook.com/tools/explorer), and select your application on far top (instead of Graph API Explorer). After that, click on "Get Access Token" to open a menu. Into "Extended Permissions", tick 'publish_actions" and validate.

A pop-up may ask the account to confirm the rights to the app. After saying yes, you're done setting up Facebook.

#Set up with twitter

###TwitterAPI
Get it on [GitHub](https://github.com/geduldig/TwitterAPI)

###Register your app
You need to register a twitter app [here](https://dev.twitter.com/apps).

###Get the IDs
You need froms your app settings in "Key and Access Token" tab, 
* the *Consumer Key (API Key)* 
* the *Consumer Secret (API Secret)*

And then click on the button below which will generate the following OAuth tokens from your account:
* the *Access Token* 
* the *Access Token Secret* 
This button also add your app ont your account's granted applications.

Also, you should visit the "Permission" tab to tick "Read an Write" in order to finish the set up.


#Set up with LinkedIn

###python-LinkedIn
You need this [module](https://github.com/ozgur/python-linkedin), still on GitHub.

###Register your app
You have to register a LikedIn [app here](https://www.linkedin.com/secure/developer)

###Get the IDs
You need in your app's details:
* *API Key* 
* *API Secret*
* *Token utilisateur OAuth* 
* *Access Token Secret* 

Nothing more! LinkedIn is now ready to use.

#Set up with Tumblr

###pytumblr
You need the [pytumblr](https://github.com/tumblr/pytumblr) API.

####Register your app
Let's [create] your own Tumblr app

###Get the IDs
Still you want 
* *OAuth consumer key* 
* *OAuth consumer secret*

Then you have to go to the [api console](https://api.tumblr.com/console/) and enter those two keys to grant the API to publish on the account you're logged with.

this gives you a code like the following one:
```
// Authenticate via OAuth
var tumblr = require('tumblr.js');
var client = tumblr.createClient({
  consumer_key: 'eqdUYkdkAk3A66v8OttkpcUyu70X5Qw7pXXXXXXXXXXXX',
  consumer_secret: '9icV4lZ7CRHkqR5vlvxoVh9g2mE4XKaXXXXXXXXXXXXXXXXXXX',
  token: 'ObbXH1keCziTqGLfdIsZBeeqI9MxDX9XXXXXXXXXXXXXXXXXXX',
  token_secret: 'jDIaHbQ7IeXJcZokf9EHk9FmxXXXXXXXXXXXXXXXXXXXXXXXXX'
});
```
So you have the *token* and the *token_secret* which are also useful.

You now have all you need for Tumblr.

__________________________________________________________________________________________________________________
*Version de Python* 2.7 <s>3.4</s> (la plupart des API actuelles ne sont pas compatible Python3)  
*Librairie RSS Python* https://pypi.python.org/pypi/feedparser  
*API Tumblr Python* https://github.com/tumblr/pytumblr  
*twitterAPI* https://github.com/geduldig/TwitterAPI  
*facebook-sdk* https://github.com/pythonforfacebook/facebook-sdk   
*requests-oauthlib* https://github.com/requests/requests-oauthlib   
*python-linkedin* https://github.com/ozgur/python-linkedin
