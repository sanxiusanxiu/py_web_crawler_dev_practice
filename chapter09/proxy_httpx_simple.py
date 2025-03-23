import httpx

def proxy_simple():
    from httpx_socks import SyncProxyTransport

    proxy = '127.0.0.1:7890'
    proxies = {
        'http://': 'http://' + proxy,
        'https://': 'https://' + proxy,
    }

    with httpx.Client(proxies=proxies) as client:
        response = client.get('https://httpbin.org/get')
        print(response.text)

def httpx_socks_sync():
    from httpx_socks import SyncProxyTransport
    # pip install httpx-socks[asyncio]

    transport = SyncProxyTransport.from_url('socks5://127.0.0.1:7891')

    with httpx.Client(transport=transport) as client:
        response = client.get('https://httpbin.org/get')
        print(response.text)

def httpx_socks_async():
    import asyncio
    from httpx_socks import AsyncProxyTransport

    transport = AsyncProxyTransport.from_url('socks5://127.0.0.1:7891')

    async def main():
        async with httpx.AsyncClient(transport=transport) as client:
            response = await client.get('https://httpbin.org/get')
            print(response.text)

    if __name__ == '__main__':
        asyncio.run(main())