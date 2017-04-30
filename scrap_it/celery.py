from celery import Celery
from scrap_it.config import CeleryConfig

app = Celery("scrap_it")
app.config_from_object(CeleryConfig)

if __name__ == '__main__':
    app.worker_main()