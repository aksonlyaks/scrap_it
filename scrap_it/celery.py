from celery import Celery
from config import CeleryConfig
from .tasks import google_maps_resturant_search

app = Celery("scrap_it")
app.config_from_object(CeleryConfig)

google_maps_resturant_search.delay()