! pip install kafka-python
!pip install s3fs
from kafka import KafkaConsumer
from time import sleep
from json import dumps,loads
import json
from s3fs import S3FileSystem


# for c in consumer:
#     print(c.value)


consumer = KafkaConsumer(
    'demo_testing2',
     bootstrap_servers=['(PublicIP):9092'], #add your IP here
    value_deserializer=lambda x: loads(x.decode('utf-8')))


s3 = S3FileSystem()!pip install s3fs

import json
from s3fs import S3FileSystem

# Configure the S3FileSystem with your AWS credentials
# Replace 'YOUR_AWS_ACCESS_KEY_ID' and 'YOUR_AWS_SECRET_ACCESS_KEY' with your actual credentials
s3 = S3FileSystem(
    key='',
    secret=''
)
for count, i in enumerate(consumer):
    with s3.open("s3://harish-kafka/stock_market_{}.json".format(count), 'w') as file:
        json.dump(i.value, file)




