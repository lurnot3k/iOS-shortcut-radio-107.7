import requests
import location
import json
import sys
# Obtenir la position actuelle
loc = location.get_location()
latitude = loc['latitude']
longitude = loc['longitude']
 
# Afficher les coordonnées pour vérification
#print(f"Latitude: {latitude}, Longitude: {longitude}")
 
# Utiliser l'API de géocodage inversé de Geoapify pour obtenir l'adresse
apiKey = 'd548c5ed24604be6a9dd0d989631f783'
url = f"https://api.geoapify.com/v1/geocode/reverse?lat={latitude}&lon={longitude}&format=json&apiKey={apiKey}"
 
response = requests.get(url).json()
 
# Initialiser le nom de la route
roadName = "Route non identifiée"
 
# Vérifier la réponse et extraire le nom de la route
if response and 'results' in response and len(response['results']) > 0:
    ref = response['results'][0].get('ref')
    roadName = ref or response['results'][0].get('street') or roadName
 
if roadName == "A 8":
    roadName = "C 8"
if roadName == "C 8" and longitude >= 6.3532277941703805:
    roadName = "B 8"
if roadName == "A 10" and latitude <= 46.58712254015235:
    roadName = "B 10"
if roadName == "A 71" and latitude <= 47.04241760252488:
    roadName = "B 71"
if roadName == "A 19" and longitude <= 3.0885314941406254:
    roadName = "B 19"
if roadName == "A 28" and latitude >= 48.4501049501674:
    roadName = "Autoroute sans radio"
if roadName == "A 20" and latitude >= 45.15203310667811:
    roadName = "Autoroute non concédée"
if roadName == "A 61" and longitude >= 1.93559467792511:
    roadName = "B 61"
if roadName == "A 63" and latitude >= 43.69375589262979:
    roadName = "B 63"
if roadName == "A 68" and latitude >= 43.72198619440862:
    roadName = "Autoroute non concédée"
if roadName == "A 89" and longitude >= 3.1845813989639287:
    roadName = "B 89"
if roadName == "A 54" and longitude >= 4.835389852523805:
    roadName = "B 54"
if roadName == "A 51" and latitude <= 43.53021885456462:
    roadName = "Autoroute non concédée"
if roadName == "A 51" and latitude >= 44.908687525898436:
    roadName = "B 51"
if roadName == "A 46" and latitude >= 45.6991809878128:
    roadName = "B 46"
if roadName == "A 40" and longitude >= 5.33212423324585:
    roadName = "B 40"
if roadName == "A 77" and latitude <= 47.41002934532879:
    roadName = "Autoroute non concédée"
if roadName == "A 6" and latitude <= 46.31268632058226:
    roadName = "B 6"
if roadName == "A 1":
    roadName = "C 1"
if roadName == "A 2":
    roadName = "C 2"
if roadName == "A 3":
    roadName = "C 3"
if roadName == "A 4":
    roadName = "C 4"
if roadName == "A 5":
    roadName = "C 5"
if roadName == "A 6":
    roadName = "C 6"
if roadName == "A 7":
    roadName = "C 7"
if roadName == "A 9":
    roadName = "C 9"

 
# Afficher le nom de l'autoroute ou de la route
#print(roadName)

sys.stdout.write(roadName)
