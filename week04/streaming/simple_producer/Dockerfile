FROM continuumio/miniconda

ADD client_simple.py .
ADD requirements.txt .

RUN pip install -r requirements.txt

ENV KAFKA_SERVER "localhost:9092"

CMD ["python","client_simple.py"]
