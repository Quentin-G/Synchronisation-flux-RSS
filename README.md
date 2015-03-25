Synchronisation-flux-RSS
========================

**Projet de Master 1 informatique.**

#Get ready
* [First needs](#needs)
* [The main app](#the-main-app)
* [User interface](#the-user-interface)
* [set up with facebok](#set-up-with-facebook)
* [set up with twitter](#set-up-with-twitter)
* [Set up with LinkedIn](#set-up-with-linkedin)
* [Set up with Tumblr](#set-up-with-tumblr)
* [Set up with WordPress](#set-up-with-wordpress)

#Needs

You just need [Python 2](https://www.python.org/downloads/) to execute the files.

For the social networks API, you may use the pip bundle

    pip install FeedSynchronizer

###Building on Unix
First download the sources on the link above.
Type "./configure" in the current directory and when it finishes, type "make".  This creates an
executable "./python"; to install in /usr/local, first do "su root" and then "make install".

Be aware of the Build instructions in python's Readme file.

###Installing on Windows
You have precompiled installers on the link above. You mays also see [here](https://docs.python.org/2.7/using/windows.html#installing-python) different ways to install

###Installing on Mac-OS
Mac OS X 10.8 comes with Python 2.7 pre-installed by Apple. Otherwise, you may see [this documentation](https://docs.python.org/2.7/using/mac.html). You also have python installers for Mac OS X [here](https://www.python.org/downloads/mac-osx/)


#The main app

###Configure rss
Fisrt of all, you need to download the 2 files : "FeedSynchronizer.py" and "SenderBase.py".
You have to create an instance of FeedSynchronizer in order to choose an RSS flux to follow.

    fs = FeedSynchronizer()
    fs.set_rss_url('http://example.com/rss')

###Confugure social networks
You may also configure the social networks you want to use, with the "init_network" function.
You need a dictionary as following:

    Network_dict = {'consumer_key':'YOUR_KEY', 'consumer_secret':'YOUR_KEY', 'oauth_token':'YOUR_KEY', 'oauth_secret':'YOUR_KEY'}

it makes a variable usable in the init_network function :

    fs.init_network('Network_name', Network_dict, true)
    
Once the modifications are done, execute FeedSynchronizer.py. You get a "config.cfg" file used by FeedSynchronizer. If you delete it, a new execution will create a new one.
FeedSynchronizer now endlessly check the RSS flux and post new instances on the configured social networks.

To end the execution, use the "stop" method on the instancied variable.

###Execution example :

    from feedSynchronizer import FeedSynchronizer
    fs = FeedSynchronizer()     /* --> create config file if it does not exist */
    twitter_dict = {'consumer_key':'YOUR_KEY', 'consumer_secret':'YOUR_KEY', 'oauth_token':'YOUR_KEY', 'oauth_secret':'YOUR_KEY'}
    fs.set_rss_url('http://example.com/rss')
    fs.init_network('Twitter', twitter_dict, true)
    fs.start()
    /* deamon running */
    message posted on Twitter
    message posted on Twitter
    fs.stop()
    /* end */
    
#The user interface

The user interface is to simply set up the application to work. You can set up the RSS link and all the social networks IDs and options.

To make it run, you will need to install the following :
* lighttpd for the server
* mod_fastcgi for the interface
* python2-flup for WSGI server

Then add these lines to the lighttpd configuration file
###/etc/lighttpd/lighttpd.conf :

    server.modules += ( "mod_fastcgi" )
    fastcgi.server = (".py" => (
    				"python-fcgi" => (
    				"socket" => "/tmp/fastcgi.socket",
    				"bin-path" => "<PATH>/web.py",
    				"check-local" => "disable",
    				"min-procs" => 1,
    				"max-procs" => 1,
    				)
    			)
    		)

... where <PATH> represent the path to the FeedSynchronizer folder.

Next you need to run the server using ``` systemctl start lighttdp ```, it will be accessible at localhost/web.py

#Set up with Facebook 

You have the solution to just [set up twitter](#set-up-with-twitter) and then link your facebook account.

Otherwise...
You need :
* facebook-sdk API for python 
* Register your own App on facebook
* Find the necessary IDs
* Grant the rights for App to publish


###facebook-sdk
Get it on [GitHub](https://github.com/pythonforfacebook/facebook-sdk), unless you used our pip bundle.

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
Get it on [GitHub](https://github.com/geduldig/TwitterAPI), unless you used our pip bundle.

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
You need this [module](https://github.com/ozgur/python-linkedin), unless you used our pip bundle.

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
You need the [pytumblr](https://github.com/tumblr/pytumblr) API, *unless* you used our pip bundle.

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

# Set up with WordPress

###WordPress xmlrpc

You need the [wordpress_xmlrpc](https://python-wordpress-xmlrpc.readthedocs.org/en/latest/) library, *unless* you used our pip bundle.
Just type in your terminal :
    pip install python-wordpress-xmlrpc
    
###Use your WP account
As a WordPress blog owner, you need a [WP account](https://signup.wordpress.com/signup/). 
Just complete the fields with your username and password, and the url of the website you want to publish on, adding "xmlrpc.php" as following :
    https://my-website/wordpress.com/xmlrpc.php

WordPress is now ready to use.

__________________________________________________________________________________________________________________
*Version de Python* 2.7 <s>3.4</s> (la plupart des API actuelles ne sont pas compatible Python3)  
*Librairie RSS Python* https://pypi.python.org/pypi/feedparser  
*API Tumblr Python* https://github.com/tumblr/pytumblr  
*twitterAPI* https://github.com/geduldig/TwitterAPI  
*facebook-sdk* https://github.com/pythonforfacebook/facebook-sdk   
*requests-oauthlib* https://github.com/requests/requests-oauthlib   
*python-linkedin* https://github.com/ozgur/python-linkedin
