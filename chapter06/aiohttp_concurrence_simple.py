import asyncio
import aiohttp
import time

def test(number):
    start = time.time()

    async def get(url):
        session = aiohttp.ClientSession()
        response = await session.get(url)
        await response.text()
        await session.close()
        return response

    async def request():
        url = 'https://ssr1.scrape.center/'
        await get(url)

    tasks = [asyncio.ensure_future(request()) for _ in range(number)]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))

    end = time.time()
    print('并发量：', number, ' 用时：', end - start)

for number in [1, 3, 5, 10, 15, 30, 50, 75, 100, 200]:
    test(number)
    time.sleep(1)

"""
并发量： 1 用时： 0.24360132217407227
并发量： 3 用时： 0.2914865016937256
并发量： 5 用时： 0.23633575439453125
并发量： 10 用时： 0.48740434646606445
并发量： 15 用时： 0.41086578369140625
并发量： 30 用时： 0.7979156970977783
并发量： 50 用时： 1.4050536155700684
并发量： 75 用时： 2.0033068656921387
并发量： 100 用时： 2.7045936584472656
并发量： 200 用时： 5.42927098274231
"""
