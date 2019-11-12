from datetime import timedelta
from celery.decorators import periodic_task

from core.views import get_and_save_joke


@periodic_task(run_every=timedelta(seconds=15))
def get_joke():
    get_and_save_joke()
