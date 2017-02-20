FROM ubuntu:latest

RUN apt-get update -y
RUN apt-get install -y --force-yes python python-dev python-setuptools software-properties-common gcc python-pip
RUN apt-get clean all

RUN pip install pyzmq
RUN pip install Flask

#ADD zmqserver.py /tmp/zmqserver.py

# Zmq Sub Server
EXPOSE 4444

#CMD ["python","/tmp/zmqserver.py"]

COPY . /app
WORKDIR /app

ENTRYPOINT ["python"]
CMD ["app.py"]
