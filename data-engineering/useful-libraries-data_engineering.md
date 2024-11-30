Reference:
- https://odsc.medium.com/the-30-most-useful-python-libraries-for-data-engineering-ec9aa91176ba

# The 30 Most Useful Python Libraries for Data Engineering

For the upcoming Data Engineering Summit on January 18th, we’ve reached out to some of the top experts in the field to speak on the topic. We observed from our discussions and research that the most popular data engineering programming languages include Python, Java, Scala, R, Julia, and C++. However, Python continues to lead the pack thanks to its growing ecosystem of libraries, tools, and frameworks for data engineering and related areas such as machine learning and data science.

Regardless of metric use, many python libraries for data engineering are useful. The importance of a Python library will depend on the content of the task at hand. Data gleaned from our upcoming summit and also the Data Engineering (DE) track at ODSC East 2023 identify these as some of the most useful and popular include:

## DATA WORKFLOW AND PIPELINE LIBRARIES
### Library: apache-airflow
The apache-airflow library is a widely used scheduler and monitors for executing and managing tasks, batch jobs, and orchestrating data pipelines. Data engineers can use it to manage tasks and dependencies within a data workflow that can handle a large number of tasks. It provides a simple UI and API that includes scripting for failure handling and error recovery, all wrapped in a high-performance framework. It allows one to define complex workflows as directed acyclic graphs (DAGs) of tasks, where the edges between tasks represent dependencies and the nodes represent the actual tasks that are to be executed.

- PyPI Page: https://pypi.org/project/apache-airflow
- Home Page: https://airflow.apache.org

### Library: luigi
First released by Spotify in 2011, Luigi is yet another open-source data pipeline Python library. Similar to Airflow, it allows DEs to build and define complex pipelines that execute a series of dependencies between tasks, ensuring that tasks are executed in the correct order while managing failures. Luigi also includes event monitoring that can trigger task execution. It can be used for ETL and data ingestion and provides data cleaning and transformation service before persisting it to data stores such as data lakes and warehouses.

- PyPI Page: https://pypi.org/project/luigi/
- Home Page: https://github.com/spotify/luigi

### Library: prefect: a library for building data pipelines
For data engineers, Airflow is a trusted tool but sometimes lacks the features necessary for the modern data stack. Prefect was designed with these shortcomings in mind. Prefect seeks to provide a simple, intuitive way to build and manage complex data workflows and pipelines. It allows data engineers to define and orchestrate pipelines, schedule, and trigger tasks, and handle error handling and retries. Similar to other workflow python libraries for data engineering, it can be used to extract data from various sources, transform and clean the data, and load it into a target system or database. It can also be used to monitor the status and progress of tasks, and provide alerts and notifications when needed.

- PyPI Page: https://pypi.org/project/prefect/
- Home Page: https://github.com/PrefectHQ/prefect/

### Library: kafka-python
Apache Kafka is a popular distributed messaging platform used for building real-time data pipelines and streaming applications that stores data and replicates it across multiple servers, providing high availability and durability in case of server failures. The Kafka-python library provides a high-level API for producing and consuming messages from Apache Kafka, as well as lower-level APIs for more advanced use cases such as asynchronous processing that facilitates sending and receiving messages without blocking the main thread of execution.

- PyPl Page: https://pypi.org/project/kafka-python
- Home Page: https://pypistats.org/packages/kafka-python

### Library: kombu
Kombu and Kafka-python are similar in that they are both libraries for working with messaging systems in Python. However, Kombu is a Python messaging library that provides a high-level API for interacting with message brokers such as RabbitMQ and AMQP and support for message serialization, connection pooling, and retry handling with these brokers. Data engineers can use Kombu to produce and consume messages from message brokers, which can be used to build data pipelines and stream data between systems such as producing data from a database and sending it to a message broker, whose messages can then be consumed by another application in the pipeline.

- PyPI Page: https://pypi.org/project/kombu
- Home Page: https://docs.celeryq.dev/projects/kombu/en/stable

## DATA ANALYSIS LIBRARIES
### Library: pandas
Pandas is one of the most popular Python libraries for working with small- and medium-sized datasets. Built on top of NumPy, Pandas (abbreviation for Python Data Analysis Library) is ideal for data analysis and data manipulation. It’s considered a must-have given its large collection of powerful features such as data merging, handling missing data, data exploration, and overall efficiency. Data engineers use it to quickly read data from various sources, perform analysis and transformation operations on the data, and output the results in various formats. Pandas is also frequently paired with other python libraries for data engineering, such as scikit-learn for data analysis and machine learning tasks.

- PyPI Page: https://pypi.org/project/pandas
- Home Page: https://pandas.pydata.org/

### Library: pyarrow
Developed by some of the same authors of Pandas (Wes McKinney), to solve some of the scalability issues of Pandas, Apache Arrow uses the now popular columnar data store for better performance and flexibility. The PyArrow library provides a Python API for the functionality provided by the Arrow libraries, along with tools for Arrow integration and interoperability with pandas, NumPy, and other software in the Python ecosystem. For data engineers, pyarrow provides a scalable library to easily integrate data from multiple sources into a single, unified, and large dataset for easy manipulation and analysis.

- PyPI Page: https://pypi.org/project/pyarrow
- Home Page: https://arrow.apache.org/

## CLOUD LIBRARIES
### Library: boto3
AWS is one of the most popular cloud service providers so there’s no surprise that boto3 is on top of the list. Boto3 is a Software Development Kit (SDK) library for programmers to write software that makes use of a long list of Amazon services including data engineer favorites such as Glue, EC2, RDS, S3, Kinesis, Redshift, and Athena. In addition to performing common tasks such as uploading and downloading data, and launching and managing EC2 instances, data engineers can leverage Boto3 to programmatically access and manage many AWS services, that can be used to build data pipelines and automate data workflow tasks.

- PyPI Page: https://pypi.org/project/boto3/
- Home Page: https://github.com/boto/boto3

### Library: google-API-core
Data engineering is performed mainly on the cloud, and Google Cloud Platform (GCP) is one of the top five providers which includes AWS, Azure, IBM, and Oracle. The google-cloud-core package wraps services are common to all Google cloud APIs such as authentication and authorization, HTTP client request and response handling, data extraction (Google Drive, etc), data transformation, and data management. For data engineers it can be used to access data from Google Cloud Storage or BigQuery, Google’s cloud-based data warehousing and analytics platform, or machine learning APIs such as Cloud ML Engine.

- PyPI Page: https://pypi.org/project/google-api-core
- Home Page: https://github.com/googleapis/python-api-core

### Library: Azure-core
From another of the top 5 cloud providers, Azure Core is a python library and API for interacting with the Azure cloud services and is used by data engineers for accessing resources and automating engineering tasks. Common tasks include submitting and monitoring batch jobs, accessing databases, data containers, and data lakes, and generally managing resources such as virtual machines and containers. A related library for Python is azure-storage-blob, a library built to manage retrieve, and store large amounts of unstructured data such as images, audio, video, or text.

- PyPI Page: https://pypi.org/project/azure-core
- Home Page: https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/core/azure-core

## DATA AND BIG DATA LIBRARIES
### Library: google-cloud-bigquery
Created by Google for doing large-scale data analysis for its search and ad business data, it was first announced in 2010. Once released, BigQuery quickly became popular for its ability to perform fast SQL queries on massive datasets (petabytes). Its performance is due to how it stores and queries data. BigQuery stores data in shards in a columnar format and its distributed query engine process queries across these shards in parallel, allowing it to query and return results on even massive datasets. Now its been widely adopted as a data warehouse and is popular due to its easy setup and intuitive interfaces

- PyPI Page: https://pypi.org/project/google-cloud-bigquery/
- Home Page: https://github.com/googleapis/python-bigquery

### Library: grpcio
Building distributed API systems or microservices are a few of the use cases that drive the popularity of the gRPC Python package. gRPC is a modern open-source high-performance Remote Procedure Call (RPC) framework that can run in any environment. Features, such as load balancing, health checks, authentication bidirectional streaming, and automatic retries, make it a powerful tool for building secure, scalable, and reliable applications. In summary, data engineers can use grpcio to build efficient, scalable data pipelines for distributed systems.

- PyPI Page: https://pypi.org/project/grpcio/
- Home Page: https://grpc.io

### Library: SQLAlchemy
SQLAlchemy is the Python SQL toolkit that provides a high-level interface for interacting with databases. It allows data engineers to query data from a database using SQL-like statements and perform common operations such as inserting, updating, and deleting data from a database. SQLAlchemy also provides support for object-relational mapping (ORM), which allows data engineers to define the structure of their database tables as Python classes and map those classes to the actual database tables. SQLAlchemy provides a full suite of well-known enterprise-level persistence patterns, designed for efficient and high-performing database access such as connection pooling and connection reuse.

- PyPI Page: https://pypi.org/project/SQLAlchemy
- Home Page: https://www.sqlalchemy.org

### Library: redis-py
Redis is a popular in-memory data store widely used in data engineering due to its ability to scale and handle high volumes of data. It can be installed locally or is already available on the major cloud providers. Redis-py is a Python library that allows users to connect to a Redis database and perform various operations such as storing and retrieving data, data transformations, and data analysis. Redis-py can also be used to automate data engineering tasks such as scheduling and integrating data from other sources including extracting data from a database or API and storing it in Redis.

- PyPI Page: https://pypi.org/project/redis
- Home Page: https://github.com/redis/redis-py

### Library: pyspark
Apache Spark is one of the most popular open-source data engineering platforms thanks to its scalable design that lets it process large amounts of data fast, and makes it ideal for tasks that require real-time processing or big data analysis including ETL, machine learning, and stream processing. It can also easily integrate with other platforms, such as Hadoop and other big data platforms, making it easier for data engineers to work with a variety of data sources and technologies. The PySpark library allows data engineers to work with a wide range of data sources and formats, including structured data, unstructured data, and streaming data.

- PyPI Page: https://pypi.org/project/pyspark
- Home Page: https://github.com/apache/spark/tree/master/python

## DATA PARSING AND ETL LIBRARIES
### Library: beautifulsoup4
Data engineering doesn’t always mean sourcing data from data stores and warehouses. Often, data has to be extracted from unstructured sources such as the web or documents. Beautiful Soup is a library that makes it easy to scrape information from web pages. It sits atop an HTML or XML parser, providing Pythonic idioms for iterating, searching, and modifying the parse tree. This makes Beautiful Soup a popular Python library for data engineering because it is easy to use and allows developers to easily extract and manipulate data from unstructured sources.

- PyPI Page: https://pypi.org/project/beautifulsoup4
- Home Page: https://www.crummy.com/software/BeautifulSoup

## MACHINE LEARNING AND DEEP LEARNING LIBRARIES
### Library: scikit-learn
Created in 2007 by David Cournapeau, Fabian Pedregosa, and Andreas Müller, scikit-learn is a Python module for machine learning built on top of SciPy and was a precursor of other frameworks such as PyTorch and Tensorflow. It’s relevant today for classification, regression, and clustering, as well as tools for preprocessing and feature engineering. This allows data engineers to build machine learning models and pipelines quickly and easily.

- PyPI Page: https://pypi.org/project/scikit-learn
- Home Page: https://scikit-learn.org/stable/

### Library: TensorFlow and Keras
TensorFlow is a well know machine-learning library that allows engineers to build and train models. It provides a flexible platform for training and serving models, with a focus on training and interfacing on deep neural nets. TensorFlow is often paired with Keras, a high-level API written in Python for building and training deep learning models. It wraps the efficient numerical computation libraries Theano and TensorFlow and allows engineers to build and train models using only a few lines of code. Data engineering can also use TensorFlow for tasks such as data preprocessing, data transformation, data analytics, and data visualization.

- PyPl Page: https://pypi.org/project/tensorflow
- Home Page: https://www.tensorflow.org
- PyPl Page: https://pypi.org/project/keras
- Home Page: https://keras.io

### Library: PyTorch
Despite massive adaption, TensoFflow offered a steep learning curve and PyTorch was created to be a more flexible and user-friendly alternative to other established deep learning frameworks. Thanks to its ease of use, PyTorch is now one of the fastest-growing platforms, providing enhanced performance and expanded integration with other tools such as NumPy, Pandas, and TensorFlow. Data engineers adapted the platform as it was one of the first to offer a dynamic computational graph framework that allows for flexible and efficient model building and training.

- PyPI Page: https://pypi.org/project/torch
- Home Page: https://pytorch.org

### Library: virtualenv
Data engineers have to work with different python libraries for data engineering and package versions, so having an isolated virtual environment is essential. Virtualenv is a tool to create separated Python environments to ensure no interference across your various system setups. Since Python 3.3, a subset of it has been integrated into the standard library under the venv module. Virtualenv is especially important for projects that have complex dependencies or that need to be run on different versions of Python.

- PyPI Page: https://pypi.org/project/virtualenv
- Home Page: https://virtualenv.pypa.io/en/latest

ENVIRONMENTS, DEPLOYMENT, AND DISTRIBUTION LIBRARIES
Library: Docker and Kubernetes
Containers like the Docker library have become essential in engineering because they make it an easy package to deploy an application or service with all of the necessary parts it needs to run in a consistent and predictable manner. This can include runtime environments (Python etc), libraries, databases, configuration files, and other dependencies. Containers like Docker are often used in combination with container orchestration tools like Kubernetes to manage the deployment and scaling of containerized applications. Kubernetes automates the deployment, scaling, and management of containerized applications allowing developers to deploy and manage applications at scale, with features such as load balancing, auto-scaling, and self-healing capabilities.

- PyPI Page: https://pypi.org/project/docker
- Home Page: https://github.com/docker/docker-py
- PyPI Page: https://pypi.org/project/kubernetes
- PyPI Page: https://kubernetes.io

### Library: Dask
Dask was created to parallelize NumPy (the prolific Python library used for scientific computing and data analysis) on multiple CPUs and has now evolved into a general-purpose library for parallel computing that includes support for Pandas DataFrames, and efficient model training on XGBoost and scikit-learn. Data engineers have also adapted Dask due to its built-in functions and parallel processing capabilities that make these large dataset tasks such as data cleaning, transformation, aggregation, analysis, and exploration (Matplotlib and Seaborn support) more efficient and faster. Data engineers can also use Dask to scale workloads via a distributed scheduler that can be used to schedule jobs across a cluster of machines.

- PyPI Page: https://pypi.org/project/dask
- Home Page: https://github.com/dask/dask

### Library: Ray
Ray, incubated at UC Berkeley, had a mission to “simplify distributed computing” and easily scale Python workloads including machine learning workloads. In particular, and similar to Dask, Ray is designed to make it easy to parallelize Python code and to build distributed applications from the ground up. Ray doesn’t try to replace popular Python workloads tools but rather provide a general low-level framework that is more of a general-purpose clustering and parallelization framework that can be used to build and run any type of distributed application. Thus, there is also a growing number of projects that integrate with Ray in order to leverage accelerated GPU and parallelized computing alongside Dask, Ludwig, spaCy, Hugging Face, and scikit-learn.

- PyPI Page: https://pypi.org/project/ray
- Home Page: https://github.com/ray-project/ray

### Library: Ansible
Another trending Python library for automation is Ansible for cloud provisioning, configuration management, application deployment, intra-service orchestration, and managing multiple servers or environments. The Ansible library is similar to other configuration management and orchestration push-based tools such as Chef, SaltStack, and Puppet. However, Ansible differs from these tools in that it is agentless and uses a simple, human-readable language (YAML) to describe automation tasks. Ansible also ensures that operations are idempotent which it defines as “An operation is idempotent if the result of performing it once is exactly the same as the result of performing it repeatedly without any intervening actions.”

- PyPI Page: https://pypi.org/project/ansible
- Home Page: https://www.ansible.com

### Library: python-jenkins and jenkinsapi
Jenkins is an established continuous integration/continuous delivery tool for automating the building, testing, and deployment of applications and services to a server. Two popular Python libraries for interacting with Jenkins are python-jenkins and jenkinsapi. In the context of data engineering, the python-jenkins library can be used to automate various tasks related to data pipelines and data processing including testing, job configuration, data ingestion, data cleansing, and data transformation. You can use the library to monitor the status of Jenkins jobs, retrieve job logs, and cancel running jobs. Similarly, the JenkinsAPI library can be used in data engineering to automate the building and deployment of data pipelines and other related tasks.

- PyPI Page: https://pypi.org/project/jenkinsapi
- Home Page: https://www.jenkins.io

## UTILITY LIBRARIES
### Library: psutil
psutil (process and system utilities) is a cross-platform library for retrieving information on running processes and system utilization (CPU, memory, disks, network, sensors) in Python. It is useful mainly for system monitoring, profiling and management of running processes. It implements many functionalities offered by classic UNIX command line tools such as ps, top, iotop, lsof, netstat, ifconfig, free, and others. For data engineering it provides a variety of tools for limiting the resources used by a process, including CPU, memory, disk, and network usage, thus allowing engineers to ensure that processes do not consume too many resources and potentially impact the performance of a system.

- PyPI Page: https://pypi.org/project/psutil/
- Home Page: https://github.com/giampaolo/psutil

### Library: urllib3
urllib3 is a powerful, user-friendly HTTP client for Python with thread safety, support for compression, client-side verification, and many other utilities that are missing from the Python standard libraries. Key functionality includes support for HTTP requests (GET, PUT, POST, DELETE), manipulating headers, enabling timeouts, and supporting cookies.

PyPI Page: https://pypi.org/project/urllib3

Home Page: https://urllib3.readthedocs.io/en/stable

### Library: python-dateutil
The need to manipulate date and time is ubiquitous in Python, and often the built-in datetime module doesn’t suffice. The dateutil module is a popular extension to the standard datetime module. If you’re seeking to implement timezones, calculate time deltas, or want more powerful generic parsing, then this library is a good choice.

- PyPI Page: https://pypi.org/project/python-dateutil
- Home Page: https://github.com/dateutil/dateutil

### Library: pyyaml
Most developers are familiar with YAM, the human-readable data serialization format that is a popular choice for storing configuration data that was originally used to build configuration files, but since it’s a serialization language, its use has expanded and is now also popular for object serialization in place of file formats such as JSON. In data engineering, pyyaml is often used to configure container orchestration, data pipelines, batch jobs, and general workflow for data processing.

PyPI Page: https://pypi.org/project/PyYAML

Home Page: https://pyyaml.org/

### Library: pyparsing
This module is a popular alternative to regular expressions and can be used to build and executed basis text parsers. It can be used for evaluating user-definable expressions, processing custom application language commands, or extracting data from formatted reports.

- PyPI Page: https://pypi.org/project/pyparsing
- Home Page: https://github.com/pyparsing/pyparsing