from celery import Celery
from config import CeleryConfig

app = Celery("scrap_it")
app.config_from_object(CeleryConfig)