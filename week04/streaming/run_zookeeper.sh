kafka-topics.sh \
  --zookeeper localhost:2181 \
  --create --topic test-topic \
  --partitions 2 \
  --replication-factor 1

kafka-topics.sh --zookeeper localhost:2181 --describe
kafka-topics.sh --zookeeper localhost:2181 --delete --topic test-topic

kafka-console-consumer.sh \
  --bootstrap-server localhost:9092 \
  --from-beginning \
  --topic test-topic

kafka-consumer-groups.sh --bootstrap-server localhost:9092 --list
