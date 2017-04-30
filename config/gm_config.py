import os
from .base_config import ApplicationConfig

# Configuration for Google Maps Places Search
class GoogleMapsConfig(ApplicationConfig):
	task_indetifier = "Google-Maps"
	task_description = "Google Maps Places API Requests"
	google_maps_api_key = os.environ.get('GOOGLE_MAPS_API_KEY')