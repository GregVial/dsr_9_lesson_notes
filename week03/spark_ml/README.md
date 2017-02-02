## Pre Requisites
### 1. You should have Java 8 installed, otherwise:
- sudo add-apt-repository ppa:webupd8team/java
- sudo apt-get update
- sudo apt-get install oracle-java8-installer

### 2. You should have Anaconda installed, otherwise:
- wget https://repo.continuum.io/archive/Anaconda2-4.2.0-Linux-x86_64.sh
- bash Anaconda2-4.2.0-Linux-x86_64.sh
- source ~/.bashrc

### 3. You should have PY4J and SPARK-SKLEARN packages installed, otherwise:
- pip install py4j
- pip install spark-sklearn

### 4. You should have MySQL installed, otherwise:
- sudo apt-get install mysql-server

### 5. You should have MySQL Connector/J JAR file available, otherwise:
- wget https://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-java-5.1.39.tar.gz
- tar -xvf mysql-connector-java-5.1.39.tar.gz 

### 6. You should have Spark 2.0 installed, otherwise:
- wget http://d3kbcqa49mib13.cloudfront.net/spark-2.0.0-bin-hadoop2.7.tgz
- tar -xvf spark-2.0.0-bin-hadoop2.7.tgz
- mv spark-2.0.0-bin-hadoop2.7 spark

### 7. If you'll be running Jupyter Notebook from an EC2 instance, you should follow these steps:
#### 7.0 Make sure the Security Group associated with your EC2 instance has the following rules:
- SSH with source Anywhere
- HTTPS with source Anywhere
- Custom TCP Rule with Port 8888 and source Anywhere

#### 7.1. Generate your own SSL Certificate
- mkdir certificates
- cd certificates
- openssl genrsa -out server.key 1024
- openssl req -new -key server.key -out server.csr
- openssl x509 -req -days 366 -in server.csr -signkey server.key -out server.crt
- cat server.crt server.key > server.pem

#### 7.2. Create Jupyter Notebook config file
- jupyter notebook --generate-config
- cd ~/.jupyter
- vi jupyter_notebook_config.py
	- c = get_config()
	- c.IPKernelApp.pylab = 'inline'
	- c.NotebookApp.certfile = '/home/ubuntu/certificates/mycert.pem'
	- c.NotebookApp.ip = '*'
	- c.NotebookApp.open_browser = False
	- c.NotebookApp.port = 8888

## Configurations
### 1. Apache Spark - you have to add packages/jars so Spark can handle XML and JDBC sources
- cd /home/ubuntu/spark/conf
- cp spark-defaults.conf.template spark-defaults.conf
- vi spark-defaults.conf
	- spark.jars.packages    com.databricks:spark-xml_2.11:0.4.0
	- spark.jars	       /home/ubuntu/mysql-connector-java-5.1.39/mysql-connector-java-5.1.39-bin.jar

### 2. Environment Variables - you have to add this variables, so you can easily run PySpark as a Jupyter Notebook
- vi ~/.bashrc
	- export JAVA_HOME="/usr/lib/jvm/java-8-oracle"
	- export SPARK_HOME="/home/ubuntu/spark"
	- export PATH="$SPARK_HOME/bin:$SPARK_HOME:$PATH"
	- export PYSPARK_DRIVER_PYTHON="jupyter"
	- export PYSPARK_DRIVER_PYTHON_OPTS="notebook"

## Class Materials
### 1. Clone the Repository
- git clone https://github.com/dvgodoy/DSR-Spark-Class.git

### 2. Run PySpark
- cd DSR-Spark-Class
- pyspark OR nohup pyspark

## Using AWS EC2 Image
### 1. Go for the EC2 menu

#### 1.1 Click on Launch Instance

#### 1.2 Look for the AMI ID ami-3bb56c5b in Community AMIs

#### 1.3 When asked for, create a new key pair - download it and keep it safe!

#### 1.4 When asked for, create a new security group with the following rules:
- SSH with source Anywhere
- HTTPS with source Anywhere
- Custom TCP Rule with Port 8888 and source Anywhere

#### 1.5 After your instance is ready, you can SSH into it:
- ssh -i mykeypairfile.pem ubuntu@ec2-XX-XX-XX-XX.us-west-2.compute.amazonaws.com

#### 1.6 Update and then install Git
- sudo apt-get update
- sudo apt-get install git

#### 1.7 Clone the repository and run PySpark, as in the "Class Materials" section
