from celery import Task
from celery.schedules import crontab

from .celery_config import app
from ..binance_api import request_to_binance_api
from ..kafka_operations.producer import send_to_topic


class BinanceApiProducer(Task):
    name = 'BinanceApiProducer'

    def run(self):
        resp_data = request_to_binance_api()
        send_to_topic(topic_name="BINANCE_API", value=resp_data)


app.register_task(BinanceApiProducer())
app.conf.beat_schedule = {
    BinanceApiProducer.name: {
        'task': BinanceApiProducer.name,
        'schedule': crontab(minute='*/2'),
    }
}
