import json
import random
import threading
import time

from kafka import KafkaConsumer, KafkaProducer
from producers import Producer, Producer2
from consumers import Consumer, Consumer2

if __name__ == '__main__':
    threads = [
        Producer(),
        Producer(),
        Producer2(),
        Producer2(),
        Consumer(),
        Consumer2(),
    ]

    for t in threads:
        t.start()
