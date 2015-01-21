#Mise en place de la publication sur facebook

Afin de pouvoir poster sur facebook à partir de l'application, il est 
nécessaire de remplir les conditions suivantes:
*Avoir installé l'API facebook-sdk
*Avoir enrgistré sa propre application facebook
*disposer des ID nécessaires au fonctionnement de l'API
*Accorder les droits de publication à l'application enregistrée

##Installer facebook-sdk
Rendez-vous sur le [GitHub de l'API](https://github.com/pythonforfacebook/facebook-sdk) afin d'installer ce module 
nécessaire à la gestion de l'API facebook via python.

##Créer son application Facebook
L'application facebook sert de filtre entre votre compte facebook et le programme.
Pour créer son application facebook, rendez-vous sur [developpers facebook](https://developers.facebook.com/), 
enregistre-vous comme développeur (nécéssite un numéro de téléphone valide), puis dans l'onglet "My Apps", sélectionner 
"Add a new App".

##Obtenir les codes d'identification
Une fois votre nouvelle application créée, vous aurez besoin de son **ACCESS_TOKEN** qui se trouve dans l'onglet 
"Tool & Support -> Access Token Debugger". L'**ACCESS_TOKEN** est de la forme:

APP ID|1ds__S2_N7gIig2THoHxxxxxxxx

Afin de permettre à votre application de poster sur votre profil (ou page), vous aurez besoin de l'**ID_USER** 
de ce dernier. Pour cela rendez-vous sur le journal ou la page, puis dans la barre d'adresse, remplacez dans l'URL le 
"www" par "graph".
La première ligne d'information "id" contient l'**ID_USER** qui nous intéresse.

##Accorder les droits de publication
Le compte facebook devra ensuite permettre à l'application facebook de publier en son nom. Pour cela, il faut se rendre sur [ce lien](https://developers.facebook.com/tools/explorer) puis sélectionner votre application en haut (à la place de Graph API Explorer). Ensuite, cliquer sur "Get Access Token" qui ouvre un menu. Dans l'onglet "Extended Permissions", cocher 'pblish_actions" et enregistrez.

Une pop-up demande à l'utilisateur de confirmer l'accès à ses informations personelles. Après validation, l'envoi de messages sur facebook devrait être fonctionnel.
