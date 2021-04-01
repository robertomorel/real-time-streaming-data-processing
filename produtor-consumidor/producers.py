import json
import random
import threading
import time

from faker import Faker
from kafka import KafkaConsumer, KafkaProducer

fake = Faker()

class Producer(threading.Thread):

    def run(self):
        producer = KafkaProducer(bootstrap_servers='localhost:9092', value_serializer=lambda v: json.dumps(v).encode('utf-8'))

        while True:
            data = {}
            id_ = random.randint(0, 1000)

            if data.__contains__(id(id_)):
                message = data.get(id_)
            else:
                streaming = {'idade': random.randint(10, 50), 'altura': random.randint(100, 200),
                            'peso': random.randint(30, 100)}
                message = [id_, streaming]
                data[id_] = message

            producer.send('topico-cadastro', message)
            #time.sleep(random.randint(0, 5))
            time.sleep(1)

class Producer2(threading.Thread):

    def run(self):
        producer = KafkaProducer(bootstrap_servers='localhost:9092', value_serializer=lambda v: json.dumps(v).encode('utf-8'))

        while True:
            data = {}
            id_ = random.randint(0, 1000)

            if data.__contains__(id(id_)):
                message = data.get(id_)
            else:
                streaming = {'nome': fake.name(), 'salario': random.randint(1000, 3000)}
                message = [id_, streaming]
                data[id_] = message

            producer.send('topico-pcs', message)
            time.sleep(4)                        