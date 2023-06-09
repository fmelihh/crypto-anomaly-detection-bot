import json
from kafka import KafkaProducer

_kafka_producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8"),
)


def send_to_topic(topic_name: str, value: dict):
    _kafka_producer.send(topic_name, value)
    _kafka_producer.flush()


__all__ = ["send_to_topic"]
