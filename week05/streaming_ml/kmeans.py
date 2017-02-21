from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt

N_CLUSTER = 3

X, y = make_blobs(n_samples=1000,
                  cluster_std=4.0,
                  centers=N_CLUSTER,
                  random_state=42)

kmeans = KMeans(n_clusters=N_CLUSTER, random_state=42)
y_pred = kmeans.fit_predict(X)

colors = ["blue", "green", "orange"]

for i in range(N_CLUSTER):
    idx = y_pred == i
    plt.scatter(X[idx, 0], X[idx, 1], c=colors[i], label=("Cluster %d" % i))

plt.legend()
plt.title('K-Means')
plt.show()
