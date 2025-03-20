import asyncio
import requests

async def request():
    url = 'https://www.baidu.com'
    status = requests.get(url)
    return status

# 创建 5 个 task
tasks = [asyncio.ensure_future(request()) for _ in range(5)]
print('task:', tasks)

loop = asyncio.get_event_loop()
# 先传递给 wait() 方法，再注册到事件循环中
loop.run_until_complete(asyncio.wait(tasks))

for task in tasks:
    print(task.result())
