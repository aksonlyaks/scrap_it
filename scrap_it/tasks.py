import googlemaps
import celery
from config import GoogleMapsConfig
from .celery import app
from celery.registry import tasks

# FIXME: Need a way to properly handle task from scheduler to worker.
# TODO: https://blog.balthazar-rouberol.com/celery-best-practices.
class BaseTask(celery.Task):
	"""This class is base for all Celery Tasks. This class can be used to perform 
	generic action e.g. logging for all tasks defined. Each method of this class
	gets executed on a special event. For more details please check method doc string.
	"""	
	
	def __call__(self, *args, **kwargs):
		"""In celery task this function call the run method, here you can
		set some environment variable before the run of the task"""
		return self.run(*args, **kwargs)

	def on_failure(self, exc, task_id, args, kwargs, einfo):
		"""In celery task this function gets invoked when a task gets `failed`.
		For arguments we can identify the task and get retrieve any extra 
		parameters passed to this function"""
		pass

	def after_return(self, status, retval, task_id, args, kwargs, einfo):
		"""In celery task this is the exit point of all tasks"""
		pass

	def on_retry(self, exc, task_id, args, kwargs, einfo):
		"""In celery task this function gets invoked when a task gets retried.
		For arguments we can identify the task and get retrieve any extra 
		parameters passed to this function"""
		pass

	def on_success(self, retval, task_id, args, kwargs):
		"""In celery task this function gets invoked when a task execute successfully."""
		pass


"""Using task decorator instead of class based tasks
is the recommended way to define concrete tasks For details check 
out following links:
https://github.com/celery/celery/issues/2758
https://github.com/celery/celery/issues/3645"""
@app.task(bind=True, base=BaseTask, name="Google Maps Place Search")
def google_maps_place_search(self):
	gmaps = googlemaps.Client(key=GoogleMapsConfig.google_maps_api_key, 
						connect_timeout = GoogleMapsConfig.connect_timeout,
						read_timeout = GoogleMapsConfig.read_timeout)
	response = gmaps.places("resturants")
	return response