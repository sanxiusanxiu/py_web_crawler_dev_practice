import pika

queue_name = 'scrape'
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

while True:
    print('请回车（Enter）。。。')
    input()
    method_frame, header, body = channel.basic_get(
        queue=queue_name, auto_ack=True)
    if body is not None:
        print(f'Get {body}')
