import pika

queue_name = 'scrape'
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
# 声明一个频道对象 channel （声明队列）
channel = connection.channel()
channel.queue_declare(queue=queue_name)

# 向队列中添加消息，routing_key 是队列名称，body 是真实消息（生产内容）
channel.basic_publish(exchange='', routing_key=queue_name, body='Hello World!')
