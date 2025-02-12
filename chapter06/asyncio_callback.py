import asyncio
import requests

# 定义request方法，注意没有打印语句
async def request():
    url = 'https://www.baidu.com'
    status = requests.get(url)
    return status

# 定义callback方法，打印task对象
def callback(task):
    print('task对象的状态：', task.result())

# 当协程对象执行完成后，再执行回调方法

# 定义协程对象
coroutine = request()
# 定义task对象
task = asyncio.ensure_future(coroutine)
# 将回调函数传递给task对象
task.add_done_callback(callback)
print('task对象：', task)
# 定义事件循环
loop = asyncio.get_event_loop()
# 将task对象注册到事件循环中
loop.run_until_complete(task)
print('task注册：', task)
print('loop')

# task对象： <Task pending name='Task-1' coro=<request() running at D:\workspace\py_web_crawler_dev_practice\chapter06\asyncio_callback.py:5> cb=[callback() at D:\workspace\py_web_crawler_dev_practice\chapter06\asyncio_callback.py:11]>
# task对象的状态： <Response [200]>
# task注册： <Task finished name='Task-1' coro=<request() done, defined at D:\workspace\py_web_crawler_dev_practice\chapter06\asyncio_callback.py:5> result=<Response [200]>>
# loop
