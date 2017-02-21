from pyspark.mllib.linalg import Vectors
from pyspark.mllib.regression import LabeledPoint
from pyspark.mllib.clustering import StreamingKMeans

def parse(lp):
    label = float(lp[lp.find('(') + 1: lp.find(')')])
    vec = Vectors.dense(lp[lp.find('[') + 1: lp.find(']')].split(','))

    return LabeledPoint(label, vec)

# format [x1, x2, x3]
training_data = sc.textFile("data/mllib/kmeans_data.txt")\
    .map(lambda line: Vectors.dense([float(x) for x in line.strip().split(' ')]))
testing_data = sc.textFile("data/mllib/streaming_kmeans_data_test.txt").map(parse)

trainingStream = ssc.queueStream([training_data])
testingStream = ssc.queueStream([test_data])
