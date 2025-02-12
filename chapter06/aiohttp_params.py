import aiohttp
import asyncio

async def main():
    url = 'https://www.httpbin.org/get'
    params = {'name': 'Tom', 'age': 24}
    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as response:
            print(await response.text())

if __name__ == '__main__':
    asyncio.run(main())
