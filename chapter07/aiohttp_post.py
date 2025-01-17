import aiohttp
import asyncio

async def main():
    url = 'https://www.httpbin.org/post'
    data = {'name': 'Tom', 'age': 24}
    async with aiohttp.ClientSession() as session:
        # POST表单提交
        async with session.post(url, data=data) as response:
        # 如果是POST JSON数据提交，需要使用json参数
        # async with session.post(url, json=data) as response:
            print(await response.text())

if __name__ == '__main__':
    asyncio.run(main())
