pip install kafka-python

import pandas as pd
from kafka import KafkaProducer, KafkaConsumer
from time import sleep
from json import dumps
import json

producer = KafkaProducer(bootstrap_servers=['(PublicIP):9092'],
                         value_serializer=lambda x:
                         dumps(x).encode('utf-8'))

producer.send('demo_testing2', value={"sarthak":"khade"})

df = pd.read_csv("indexProcessed.csv")


df.head()

while True:
    dict_stock = df.sample(1).to_dict(orient="records")[0]
    producer.send('demo_testing2', value=dict_stock)
    sleep(1)

producer.flush() #clear data from kafka server
