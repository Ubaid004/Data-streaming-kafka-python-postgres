
from faker import Faker
import time
import schedule
import random
from kafka import KafkaProducer
from json import dumps


kafka_nodes="kafka:9092"
my_topics="weather"

def gen_data():
	faker=Faker()

	prod=KafkaProducer(bootstrap_servers=kafka_nodes, value_serializer=lambda x:dumps(x).encode("utf-8"))

	data={"city" : faker.city(), "temprature": random.uniform(10.0, 90.0)}

	print(data)

	prod.send(topic=my_topics, value=data)

	prod.flush()


if __name__ == "__main__" :
	gen_data()
	schedule.every(10).seconds.do(gen_data)

while True:
	schedule.run_pending()
	time.sleep(0.5)

