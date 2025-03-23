import asyncio
import aiohttp

def proxy_simple():
    # proxy = '127.0.0.1:7890'
    proxy = 'http://username:password@127.0.0.1:7890'

    async def main():
        async with aiohttp.ClientSession() as session:
            async with session.get('https://httpbin.org/get', proxy=proxy) as response:
                print(await response.text())

    if __name__ == '__main__':
        asyncio.run(main())

def proxy_socks():
    from aiohttp_socks import ProxyConnector

    connector = ProxyConnector.from_url('socks5://127.0.0.1:7891')

    async def main():
        async with aiohttp.ClientSession(connector=connector) as session:
            async with session.get('https://httpbin.org/get') as response:
                print(await response.text())

    if __name__ == '__main__':
        asyncio.run(main())
