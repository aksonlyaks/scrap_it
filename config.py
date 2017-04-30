import os

# Celery Configuration
class CeleryConfig:
	enable_utc = True
	broker_url = os.environ['CELERY_BROKER_URL']
	result_backend = os.environ['CELERY_RESULT_BACKEND']
	task_always_eager = os.environ.get('CELERY_ALWAYS_EAGER', True)

# Generic Config Variables
class ApplicationConfig:
	read_timeout = 30.0
	connect_timeout = 5.0

# Task Specific Config
class GoogleMapsConfig(ApplicationConfig):
	task_indetifier = "Google-Maps"
	task_description = "Google Maps Places API Requests"
	google_maps_api_key = os.environ['GOOGLE_MAPS_API_KEY']