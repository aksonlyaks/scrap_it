import googlemaps
import requests
from celery import app
from scrap_it.config import GoogleMapsConfig

# TODO: https://blog.balthazar-rouberol.com/celery-best-practices
@app.task(bind=True, name="Google Maps Places Search")
def google_maps_resturant_search(self):
	gmaps = googlemaps.Client(key=GoogleMapsConfig.google_maps_api_key, 
							connect_timeout = GoogleMapsConfig.connect_timeout
							read_timeout = GoogleMapsConfig.read_timeout)
	response = gmaps.places("resturants")