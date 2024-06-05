# Raccourci iOS radio autoroute 107.7

**Contexte** : En France la fréquence radio utilisée pour l'info traffic est toujours la même sur tout le territoire, pratique ! Or ce n'est pas forcément le cas pour tout le monde.
Certains autoradios empêchent l'utilisation de la radio en même temps que celle du carplay, impossible donc de savoir sur quelle radio autoroutière se mettre (il en existe plus de 10 et plusieurs sur le même réseau.

**Inrérêt du script** : Ce script permet de localiser l'individu et de le connecter sur la bonne station d'autoroute en fonction du tronçon emprunté. 

# Mise en place

Le repo est composé de deux fichier primordiaux : un script en python (trouve l'autoroute sur laquelle on est) et un raccourci iOS (selon l'autoroute joue la station sur une appli de radio par internet)

**Prérequis** : 

- un iPhone disposant d'iOS 13.0 au minimum
- L'application [myTuner Radio](https://apps.apple.com/fr/app/radio-fm-mytuner-radio-france/id520502858)
- L'application [Pythonista 3](https://apps.apple.com/fr/app/pythonista-3/id1085978097) (payante à 9.99€)

**Installation** : 

1. Télécharger les deux fichiers sur votre appareil
2. Ouvrir le fichier de raccourci et l'importer dans l'appli raccourci
3. Importer le fichier python (autoroute.py) sur Pythonista 3 et vérifier son bon fonctionnement en l'exécutant
4. Vérifier que la première ligne du raccourci soit configurée avec le bon raccourci 


<img src="https://github.com/lurnot3k/iOS-shortcut-radio-107.7/assets/77621024/5cffe1a5-5711-4c58-9982-21c2d3702ced" alt="Raccourci" width="200"/>

# Informations complémentaire

Le scrit est "mal écrit" en raison des limitations imposées par Apple Shortcuts, il reste néanmoins complètement fonctionnel mais certaines autoroutes ont dues être renommées dans le code pour que cela fonctionne

**Sources**

https://static.wikia.nocookie.net/routes/images/1/15/WS_15_Concessions.jpg/revision/latest?cb=20150318125445
https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgy5Kw9jQfAzSeUvlbgT5hjGwAlOWhzB7s7uQG8xNlVwAklYH8SW0nyrQh0InXc2WGA0MhcIqD4W8vslvD-71pMA-PNdljWiAC1ct2ISkjBGlbfWzSVg44-9qXk13LVYV6sOIm5ZSF3Y4M/s1600/107.7+Carte+%253B+%2528002%2529.png (plus à jour mais utile pour SANEF)
https://routes.fandom.com/wiki/Radio_Vinci_Autoroutes
https://routes.fandom.com/wiki/Autoroute_Info?so=search
