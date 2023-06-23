from celery import Task
from celery.schedules import crontab
from .celery_config import app

from ..enums import KafkaTopics
from ..kafka_operations.consumer import consume_from_topic


class BinanceApiConsumer(Task):
    name = "BinanceApiConsumer"

    def run(self):
        consume_from_topic(KafkaTopics.BINANCE_API)


app.register_task(BinanceApiConsumer())
app.conf.beat_schedule = {
    BinanceApiConsumer.name: {
        "task": BinanceApiConsumer.name,  # Path to the Task2 class
        "schedule": crontab(minute="*/5"),
    }
}
