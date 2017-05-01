import os

# Celery Configuration
class CeleryConfig:
	broker_url = os.environ['CELERY_BROKER_URL']
	result_backend = os.environ['CELERY_RESULT_BACKEND']
	enable_utc = True
	imports = ('scrap_it.tasks')
	task_always_eager = os.environ.get('CELERY_ALWAYS_EAGER', True)
	database_table_names = {'task': 'scrap_taskmeta','group': 'scrap_groupmeta',}