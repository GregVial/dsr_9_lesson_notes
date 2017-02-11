from kafka import KafkaProducer
from time import sleep
import json
from _datetime import datetime

KAFKA_SERVER = "localhost:9092"

producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER,
                         client_id="Test Producer",
                         compression_type="gzip",# Better to compress, json is very inefficient
                         value_serializer=lambda m: bytes(json.dumps(m), 'utf-8'))


for i in range(10):
    sleep(2)
    msg = {
        "time": str(datetime.now()),
        'msg': "That is the time now"
    }
    producer.send("test-topic", msg)#bytes(json.dumps(msg), 'utf-8')
