from kafka import KafkaConsumer
import os

KAFKA_SERVER = os.environ.get("KAFKA_SERVER","localhost:9092")

consumer = KafkaConsumer(bootstrap_servers=KAFKA_SERVER,
			client_id="simple_consumer"
#			value_deserializer=lambda val: json.loads(val.decode('utf-8')),
#			group_id = "simple_consumer_group"
			)

consumer.subscribe(["test-topic"])

for msg in consumer:
	topic = msg.topic
	print(msg)
	#consumer.seek_to_beginning()
