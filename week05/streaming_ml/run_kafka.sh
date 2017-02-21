sudo docker run -p 2181:2181 -p 9092:9092 \
       --env ADVERTISED_HOST=0.0.0.0 \
       --env ADVERTISED_PORT=9092 \
       --env CONSUMER_THREADS=2 \
       spotify/kafka
