    predictionStream = model.predictOn(testStream)
    # predictionStream.pprint()

    def printResults(rdd):
        predictions = rdd.collect()
        print("Predictions: %r" % predictions)
        print("Weights %r" % model._model.weights)

    predictionStream.foreachRDD(printResults)
