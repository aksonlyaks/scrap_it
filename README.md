# Scrap_It

Scrap data from Google Maps Places using Celery task Queue.

# Installation and Running

 - Clone the Repository : `git clone git@github.com:sohaibfarooqi/scrap_it.git`
 
 - Create Virtual Environment (Recommended):
 	- `virtualenv -p <path-to-python-executable> venv`
 	- source venv/bin/activate

- Install Dependencies `pip install -r requirements.txt`

- Set up following Environment Variables:
	- `CELERY_BROKER_URL`
	- `CELERY_RESULT_BACKEND`
	- `CELERY_ALWAYS_EAGER`
	- `CELERY_EAGER_PROPAGATES`
	- `ENV`
	- `GOOGLE_MAPS_API_KEY`

Now you are ready to execute celery worker.

Start Flower Monitoring dashboard (Optional):
`flower -A scrap_it --port=5555`

To start celery worker execute followiing command: 
`celery -A scrap_it worker -l info`

Finally start celery beat:
`celery -A scrap_it beat -l info`