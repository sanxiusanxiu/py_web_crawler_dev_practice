import pika

queue_name = 'scrape'
max_priority = 100
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_delete(queue=queue_name)
channel.queue_declare(queue=queue_name,
                      arguments={'x-max-priority': max_priority},
                      durable=True)

while True:
    data, priority = input().split()
    # 向队列中添加消息，routing_key 是队列名称，body 是真实消息（生产内容）
    channel.basic_publish(exchange='',
                          routing_key=queue_name,
                          properties=pika.BasicProperties(priority=int(priority), delivery_mode=2),
                          body=data)
    print(f'put {data}')
