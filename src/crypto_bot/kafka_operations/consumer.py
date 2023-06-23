import json
from kafka import KafkaConsumer

_kafka_consumer = KafkaConsumer(
    bootstrap_servers="localhost:9092",
    enable_auto_commit=True,
    auto_offset_reset="earliest",
    consumer_timeout_ms=5000,
    value_deserializer=lambda x: json.loads(x.decode("utf-8")),
)


def consume_from_topic(topic_name: str):
    _kafka_consumer.subscribe(topic_name)
    for data in _kafka_consumer:
        print(data)

    _kafka_consumer.unsubscribe()


__all__ = ["consume_from_topic"]
