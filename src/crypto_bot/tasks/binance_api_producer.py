from celery import Task
from celery.schedules import crontab
from .celery_config import app


class BinanceApiProducer(Task):
    name = 'BinanceApiProducer'

    def run(self):
        print("task 1")


app.register_task(BinanceApiProducer())
app.conf.beat_schedule = {
    BinanceApiProducer.name: {
        'task': BinanceApiProducer.name,  # Path to the Task2 class
        'schedule': crontab(minute='*/10'),
    }
}
