from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from kafka import SimpleProducer, KafkaClient

access_token = ""
access_token_secret =  ""
consumer_key =  ""
consumer_secret =  ""

#setting up authorization
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

class MyStreamListner(StreamListener):
    def on_status(self, status):
        producer.send_messages("BigData", (status.text).encode())
        print (status.text)
        return True
    def on_error(self, status):
        print (status.text)

#initializing a kafka producer
kafka = KafkaClient("localhost:9092")
producer = SimpleProducer(kafka)
l = MyStreamListner()

stream = Stream(auth, l)
while True:
    try:
        stream.filter(languages=["en"], track=["Hadoop", "Big Data", "Machine Learning"])
    except:
        continue
