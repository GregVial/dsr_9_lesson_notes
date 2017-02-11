from kafka import KafkaProducer
from time import sleep
import json
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import make_classification
import numpy as np
from _datetime import datetime

KAFKA_SERVER = "localhost:9092"

producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER,
                         client_id="Classification Producer",
                         compression_type="gzip",# Better to compress, json is very inefficient
                         value_serializer=lambda m: bytes(json.dumps(m), 'utf-8'))


while True:
#	X = np.random.rand(200)
#	X = X.reshape(-1,2)
#	y = np.random.binomial(1,.1,100)
# Simple equivalent
	X,y = make_classification(flip_y=.1)

	lr = LogisticRegression()
	lr.fit(X,y)
	y_pred = lr.predict(X)
	score = np.mean(y_pred == y)
	
	rows = []
	for i ,row in enumerate(X):
		data_point={
			'x': row.tolist(),
			'label': y[i]
		}
		rows.append(data_point)
	msg = {"Score" : score}#,
#	       "Data" : rows}
	producer.send("test-topic",msg)
	sleep(0.5)

