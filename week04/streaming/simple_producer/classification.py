from kafka import KafkaProducer
from time import sleep
import json
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import make_classification
import numpy as np
import pandas as pd
from _datetime import datetime
from io import StringIO

KAFKA_SERVER = "localhost:9092"

def serialize(msg):
	try:
		encoded_msg = bytes(json.dumps(msg),'utf-8')
	except Exception as e:
		print(repr(e))
	else:
		return encoded_msg

producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER,
                         client_id="Classification Producer",
#			 compression_type="gzip",
			value_serializer=lambda m: serialize(m)
			)


while True:
	X,y = make_classification(n_samples=10,n_features=5,flip_y=.1)

	lr = LogisticRegression()
	lr.fit(X,y)
	y_pred = lr.predict(X)
	score = np.mean(y_pred == y)
	
	rows = []
	for i ,row in enumerate(X):
		data_point={
			'x': row.tolist(),
			'label': int(y[i])
		}
		rows.append(data_point)

	msg = {"rows" : rows,
	      "score" : score}
	producer.send("class-topic",msg)
	sleep(10)

