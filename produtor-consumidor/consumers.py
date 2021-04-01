import json
import random
import threading
import time

from kafka import KafkaConsumer, KafkaProducer

class Consumer(threading.Thread):

    def run(self):
        stream = KafkaConsumer(bootstrap_servers='localhost:9092', auto_offset_reset='latest')
        
        stream.subscribe(['topico-cadastro'])
        
        for tuple in stream: 
            obj = json.loads(tuple.value)[1]
            imc = obj['peso'] / (obj['altura']/100)**2

            if imc > 35:
                print('----- Consumidor 1 ------------------------------')
                print(imc)
                print(obj)

class Consumer2(threading.Thread):

    def run(self):
        stream = KafkaConsumer(bootstrap_servers='localhost:9092', auto_offset_reset='latest')
        
        stream.subscribe(['topico-pcs'])
        
        for tuple in stream:
            obj = json.loads(tuple.value)[1]
                 
            if obj['salario'] > 2000:
              print('----- Consumidor 2 ------------------------------') 
              print(obj) 
              print(obj['nome'])          