import asyncio
import requests
import time

start = time.time()

async def request():
    url = 'https://www.httpbin.org/delay/5'
    response = await requests.get(url)

tasks = [asyncio.ensure_future(request()) for _ in range(10)]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

end = time.time()
print('用时：', end - start)
# TypeError: object Response can't be used in 'await' expression
