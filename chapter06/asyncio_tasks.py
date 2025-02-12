import asyncio
import requests

async def request():
    url = 'https://www.baidu.com'
    status = requests.get(url)
    return status

# 创建5个task
tasks = [asyncio.ensure_future(request()) for _ in range(5)]
print('task:', tasks)

loop = asyncio.get_event_loop()
# 先传递给wait()方法，再注册到事件循环中
loop.run_until_complete(asyncio.wait(tasks))

for task in tasks:
    print(task.result())

# task: [<Task pending name='Task-1' coro=<request() running at D:\workspace\py_web_crawler_dev_practice\chapter06\asyncio_tasks.py:4>>, <Task pending name='Task-2' coro=<request() running at D:\workspace\py_web_crawler_dev_practice\chapter06\asyncio_tasks.py:4>>, <Task pending name='Task-3' coro=<request() running at D:\workspace\py_web_crawler_dev_practice\chapter06\asyncio_tasks.py:4>>, <Task pending name='Task-4' coro=<request() running at D:\workspace\py_web_crawler_dev_practice\chapter06\asyncio_tasks.py:4>>, <Task pending name='Task-5' coro=<request() running at D:\workspace\py_web_crawler_dev_practice\chapter06\asyncio_tasks.py:4>>]
# <Response [200]>
# <Response [200]>
# <Response [200]>
# <Response [200]>
# <Response [200]>
