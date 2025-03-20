def httpx_http_version():
    import httpx

    client = httpx.Client(http2=True)
    response = client.get("https://www.httpbin.org/get")
    # print(response.text)
    print(response.http_version)

# httpx_http_version()

import httpx
import asyncio
async def async_fetch(url):
    async with httpx.AsyncClient(http2=True) as client:
        response = await client.get(url)
        print(response.text)

if __name__ == '__main__':
    asyncio.run(async_fetch("https://www.httpbin.org/get"))
