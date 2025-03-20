import asyncio
import aiohttp
import time

start = time.time()

async def get(url):
    session = aiohttp.ClientSession()
    # 这里我们使用了 await，后面跟着 get 方法
    response = await session.get(url)
    await response.text()
    await session.close()
    return response

async def request():
    url = 'https://www.httpbin.org/delay/5'
    print('Waiting for:', url)
    response = await get(url)
    print('Response:', response)

tasks = [asyncio.ensure_future(request()) for _ in range(10)]
loop = asyncio.get_event_loop()
# 如果遇到 await，就会将当前协程挂起，转而执行其他协程，直到其他协程也挂起或执行完毕，再执行下一个协程
loop.run_until_complete(asyncio.wait(tasks))

end = time.time()
print('用时：', end - start)
# 用时： 6.60272216796875
