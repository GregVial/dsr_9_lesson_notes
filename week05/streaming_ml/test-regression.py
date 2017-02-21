import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import json

file = open("batches.json","r")
json_content = file.read()
file.close()
content = json.loads(json_content)

X = np.zeros((300,5))
y = np.zeros(300)
known = np.zeros(300)
#print(known)
i=0
for k,v in content.items():
	for dicty in v:
		#print(dicty["x"])
		X[i,:] = dicty["x"]
		try:
			y[i] = np.float(dicty["label"])
		except Exception as e:
			y[i] = None
		if dicty["known"] == True:
			known[i] = 1
		i+=1

unknown = 1 - known
known=known.astype(np.bool)
unknown = unknown.astype(np.bool)
#print(known)
X_train = X[known]
y_train = y[known]
lr = LinearRegression()
lr.fit(X_train,y_train)
#print(X.shape,y.shape)
#print(X_train.shape,y_train.shape)

X_test = X[unknown]
y_pred = lr.predict(X_test)
print(y_pred)
