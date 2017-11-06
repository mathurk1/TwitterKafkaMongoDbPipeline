from pymongo import MongoClient
from kafka import KafkaConsumer

# To consume latest messages and auto-commit offsets
consumer = KafkaConsumer('BigData',
                         group_id='BigData',
                         bootstrap_servers=['localhost:9092'])

# Setup MongoDB client to connect to the database
client = MongoClient()
db = client['KafkaTweets']

# Processing through each message received
for message in consumer:
    #Since we are decoding the byte string into utf-8, we need a try catch block as certain illegal characters can throw an error and stop processing
    try:
        row = {"Topic": message.topic, "Partition": message.partition, "Offset": message.offset,"Key": message.key, "Value": str(message.value, 'utf-8')}
        result = db.Tweets.insert_one(row)
    except:
        continue