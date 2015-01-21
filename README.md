Synchronisation-flux-RSS
========================

**Projet de Master 1 informatique.**

(not runnable yet)

##Set up on Facebook

You need :
*facebook-sdk API for python 
*Register your own App on facebook
*Find the necessary IDs
*Grant the rights for App to publish

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


*Version de Python* 2.7 <s>3.4</s> (la plupart des API actuelles ne sont pas compatible Python3)  
*Librairie RSS Python* https://pypi.python.org/pypi/feedparser  
*API Tumblr Python* https://github.com/tumblr/pytumblr  
*twitterAPI* https://github.com/geduldig/TwitterAPI  
*facebook-sdk* https://github.com/pythonforfacebook/facebook-sdk   
*requests-oauthlib* https://github.com/requests/requests-oauthlib   
*python-linkedin* https://github.com/ozgur/python-linkedin
