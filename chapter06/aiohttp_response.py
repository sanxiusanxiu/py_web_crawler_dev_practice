import aiohttp
import asyncio

async def main():
    url = 'https://www.httpbin.org/post'
    data = {'name': 'Tom', 'age': 24}
    async with aiohttp.ClientSession() as session:
        async with session.post(url, data=data) as response:
            print('状态码：', response.status)
            print('响应头：', response.headers)
            # 返回的是协程对象就需要加await
            print('响应体：', await response.text())
            print('响应体二进制内容：', await response.read())
            print('响应体JSON内容：', await response.json())

if __name__ == '__main__':
    asyncio.run(main())
