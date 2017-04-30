import os

# Celery Configuration
class CeleryConfig:
	enable_utc = True
	broker_url = os.environ['CELERY_BROKER_URL']
	result_backend = os.environ['CELERY_RESULT_BACKEND']
	task_always_eager = os.environ.get('CELERY_ALWAYS_EAGER', True)