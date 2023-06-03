from celery import Task
from celery.schedules import crontab
from .celery_config import app


class BinanceApiConsumer(Task):
    name = 'BinanceApiConsumer'

    def run(self):
        print("task 1")


app.register_task(BinanceApiConsumer())
app.conf.beat_schedule = {
    BinanceApiConsumer.name: {
        'task': BinanceApiConsumer.name,  # Path to the Task2 class
        'schedule': crontab(minute='*/5'),
    }
}
