import asyncio
import requests

# 定义 request 方法，注意没有打印语句
async def request():
    url = 'https://www.baidu.com'
    status = requests.get(url)
    return status

# 定义 callback 方法，打印 task 对象
def callback(task):
    print('task 对象的状态：', task.result())

# 当协程对象执行完成后，再执行回调方法

# 定义协程对象
coroutine = request()
# 定义 task 对象
task = asyncio.ensure_future(coroutine)
# 将回调函数传递给 task 对象
task.add_done_callback(callback)
print('task 对象：', task)
# 定义事件循环
loop = asyncio.get_event_loop()
# 将 task 对象注册到事件循环中
loop.run_until_complete(task)
print('task 注册：', task)
print('loop')

# task 对象： <Task pending name='Task-1' coro=<request() running at D:\workspace\crawler_async\async_callback.py:5> cb=[callback() at D:\workspace\crawler_async\async_callback.py:11]>
# task 对象的状态： <Response [200]>
# task 注册： <Task finished name='Task-1' coro=<request() done, defined at D:\workspace\crawler_async\async_callback.py:5> result=<Response [200]>>
# loop
