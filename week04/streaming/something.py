#!/usr/bin env python
# -*- coding: utf-8 -*-

from pyspark.streaming.kafka import KafkaUtils
from pyspark import SparkContext
from pyspark.streaming import StreamingContext

if __name__ == "__main__":
    # Create a local StreamingContext with two working thread
    # and batch interval of 1 second
    sc = SparkContext("local[1]", "Word Count")
    # 2nd argument is batch duration
    ssc = StreamingContext(sc, 1)

    directKafkaStream = KafkaUtils.createDirectStream(ssc,
                                                      ["test-topic"],
                                                      {"metadata.broker.list": "localhost:9092"})

    directKafkaStream.pprint()
    ssc.start()
    ssc.awaitTermination()
