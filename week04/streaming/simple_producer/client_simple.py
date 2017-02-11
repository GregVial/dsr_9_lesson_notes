from kafka import KafkaProducer

KAFKA_SERVER = "localhost:9092"

producer = KafkaProducer(bootstrap_servers = KAFKA_SERVER,
			 client_id="Test Producer")

producer.send("test-topic", b"Hi, my name is Pepe the frog!")
