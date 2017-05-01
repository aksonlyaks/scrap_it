import os
from celery.schedules import crontab

# Celery Configuration
class CeleryConfig:
	broker_url = os.environ['CELERY_BROKER_URL']
	result_backend = os.environ['CELERY_RESULT_BACKEND']
	enable_utc = True
	timezone = "UTC"
	imports = ('scrap_it.tasks')
	task_always_eager = os.environ.get('CELERY_ALWAYS_EAGER', False)
	task_eager_propagates = os.environ.get('CELERY_EAGER_PROPAGATES', False)
	task_serializer = 'json'
	database_table_names = {'task': 'scrap_taskmeta','group': 'scrap_groupmeta',}
	beat_schedule = {'run-every-30-seconds':{'task':'google_maps_place_search', 'schedule':crontab(minute='*/1')}}