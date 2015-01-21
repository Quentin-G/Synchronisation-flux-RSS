Synchronisation-flux-RSS
========================

**Projet de Master 1 informatique.**

(not runnable yet)

#Get ready
* [set up with facebok](#set-up-with-facebook)
* [set up with twitter](#set-up-with-twitter)
* [Set up with LikedIn](#set-up-with-likedin)

#Set up with Facebook

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
And then:
* the *Access Token* 
* the *Access Token Secret* 
of your own account to allow the app to publish on its name.

Eventually, you should visit the "Permission" tab to tick "Read an Write".

###Grant the access to your account

Coming soon...

#Set up with LikedIn

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



__________________________________________________________________________________________________________________
*Version de Python* 2.7 <s>3.4</s> (la plupart des API actuelles ne sont pas compatible Python3)  
*Librairie RSS Python* https://pypi.python.org/pypi/feedparser  
*API Tumblr Python* https://github.com/tumblr/pytumblr  
*twitterAPI* https://github.com/geduldig/TwitterAPI  
*facebook-sdk* https://github.com/pythonforfacebook/facebook-sdk   
*requests-oauthlib* https://github.com/requests/requests-oauthlib   
*python-linkedin* https://github.com/ozgur/python-linkedin
