import pika

queue_name = 'scrape'
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
# 声明一个频道对象 channel （声明队列）
channel = connection.channel()
channel.queue_declare(queue=queue_name)

def callback(ch, method, properties, body):
    print(f'get {body}')

# 取出消息（消费内容）
# 其中 on_message_callback 设置回调方法，auto_ack 表示自动通知消息队列当前消息已经被处理，可以移除这个消息
channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
channel.start_consuming()
