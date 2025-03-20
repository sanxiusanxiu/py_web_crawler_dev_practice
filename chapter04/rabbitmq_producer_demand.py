import pika

queue_name = 'scrape'
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue=queue_name)

while True:
    data = input()
    # 向队列中添加消息，routing_key 是队列名称，body 是真实消息（生产内容）
    channel.basic_publish(exchange='',
                          routing_key=queue_name,
                          body=data)
    print(f'put {data}')
