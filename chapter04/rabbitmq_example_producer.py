import pika
import requests
import pickle

max_priority = 100
total = 100
queue_name = 'scrape_queue'

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue=queue_name, durable=True)

for i in range(1, total + 1):
    url = f'https://ssr1.scrape.center/detail/{i}'
    request = requests.Request('GET', url)
    channel.basic_publish(exchange='',
                          routing_key=queue_name,
                          properties=pika.BasicProperties(delivery_mode=2),
                          body=pickle.dumps(request))
    print(f'put request of {url}')
