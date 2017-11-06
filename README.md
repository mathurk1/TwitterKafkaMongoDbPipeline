# TwitterKafkaMongoDbPipeline

In this project I have setup a simple data pipeline using Kafka. I have a single cluster - single broker running on an Ubuntu box in the Google Cloud Platfrom.

We have used
```
Kafka Version = 0.11
Python Version = 3.5.2
MongoDB Version = 2.6.10
```

For this I have a 
  * kafka producer which streams tweets using tweepy and feeds it into the topics
  * kafka consumer which receives the tweets and stores it in a MongoDB database


To start the process we perform the following
```
#create a topic (in the kafka installation folders which has the bin directory)
bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic BigData

#start zookeeper
bin/zookeeper-server-start.sh config/zookeeper.properties

#start kafka
bin/kafka-server-start.sh config/server.properties

#start kafka producer (in the python virtual env)
python producer.py

#start kafka consumer
python consumer.py
```

After this we can see the tweets being stored in the MongoDB database. Here is a sample output:

```
{
        "_id" : ObjectId("59ffa3f8d4fdab2bef6f8aed"),
        "Key" : null,
        "Value" : "“Top 6 Cheat Sheets Novice Machine Learning Engineers Need” by @cdossman https://t.co/hZ9b5hxzsV",
        "Offset" : 852,
        "Topic" : "BigData",
        "Partition" : 0
}
{
        "_id" : ObjectId("59ffa3fad4fdab2bef6f8aee"),
        "Key" : null,
        "Value" : "RT: KirkDBorne: Getting Started with #MachineLearning — courses, books,... https://t.co/nhqKnFSljx #BigData #Data… https://t.co/dxJGZT5AWU",
        "Offset" : 853,
        "Topic" : "BigData",
        "Partition" : 0
}
{
        "_id" : ObjectId("59ffa3fbd4fdab2bef6f8aef"),
        "Key" : null,
        "Value" : "RT @Ronald_vanLoon: 10 Free Must-Read Books for Machine Learning and Data Science | #DataScience #MachineLearning #RT… ",
        "Offset" : 854,
        "Topic" : "BigData",
        "Partition" : 0
}
{
        "_id" : ObjectId("59ffa402d4fdab2bef6f8af0"),
        "Key" : null,
        "Value" : "RT @Carestream: 'Bring your own data' may be the next big trend seen with patients in healthcare! #patientcare #healthcareIT… ",
        "Offset" : 855,
        "Topic" : "BigData",
        "Partition" : 0
}
```

References:
  * https://www.youtube.com/watch?v=fXEMB6-LiHw
  * https://kafka.apache.org/documentation
  * http://kafka-python.readthedocs.io/en/master/usage.html#
  * https://docs.mongodb.com/getting-started/python/



