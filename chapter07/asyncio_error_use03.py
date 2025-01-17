import asyncio
import requests
import time

start = time.time()

async def get(url):
    return requests.get(url)

async def request():
    url = 'https://www.httpbin.org/delay/5'
    print('Waiting for', url)
    response = await get(url)
    print('Response:', response)

tasks = [asyncio.ensure_future(request()) for _ in range(10)]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

end = time.time()
print('用时：', end - start)
# 用时： 61.90195631980896
