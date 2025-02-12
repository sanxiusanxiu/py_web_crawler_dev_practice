import asyncio
import requests
import time

start = time.time()

async def request():
    url = 'https://www.httpbin.org/delay/5'
    response = requests.get(url)
    # print(response.text)

tasks = [asyncio.ensure_future(request()) for _ in range(10)]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

end = time.time()
# 用时： 62.95824193954468
print('用时：', end - start)
