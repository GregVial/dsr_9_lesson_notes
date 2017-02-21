from kafka import KafkaConsumer
import os
import json
import pandas as pd
import numpy as np
from io import StringIO

KAFKA_SERVER = os.environ.get("KAFKA_SERVER","localhost:9092")

def deserializer(msg):
	try:
		decoded_msg = json.loads(msg.decode('utf-8'))
	except Exception as e:
		print(repr(e))
	else:
		return(decoded_msg)
		


consumer = KafkaConsumer(bootstrap_servers=KAFKA_SERVER,
			client_id="class_consumer",
			value_deserializer=lambda val: deserializer(val),
			group_id = "class_consumer_group"
			)

consumer.subscribe(["class-topic"])

for msg in consumer:
	#topic = msg.topic
	#topic = json.loads(msg.decode('utf-8'))
	#print(msg)
	#consumer.seek_to_beginning()
	#X = pd.read_csv(StringIO(msg["Score"]), sep="\s+")
	#print(X.shape)

	value = msg.value
	print(repr(msg))
	assert "rows" in value and "score" in value
	rows = value["rows"]
	score = value["score"]

	n, m = len(rows), len(rows[0]["x"])

	X = np.empty((n, m), dtype=float)
	y = np.empty((n), dtype=int)

	for i in range(n):
		row = rows[i]
		X[i, :] = row["x"]
		y[i] = row["label"]

	print("X: %r\ny: %r" % (X, y))
