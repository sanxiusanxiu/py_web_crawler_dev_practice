import pika
import requests
import pickle

max_priority = 100
queue_name = 'scrape_queue'

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
session = requests.Session()

def scrape(request):
    try:
        response = session.send(request.prepare())
        print(f'success scraped {response.url}')
    except requests.RequestException:
        print(f'error occurred when scraping {request.url}')

while True:
    method_frame, header, body = channel.basic_get(
        queue=queue_name, auto_ack=True)
    if body is not None:
        request = pickle.loads(body)
        print(f'get {request}')
        scrape(request)

