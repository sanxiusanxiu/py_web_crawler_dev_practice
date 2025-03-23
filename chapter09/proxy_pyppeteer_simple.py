import asyncio
from pyppeteer import launch

def proxy_simple():
    proxy = '127.0.0.1:7890'
    async def main():
        browser = await launch({'args': ['--proxy-server=https://' + proxy], 'headless': False})
        page = await browser.newPage()
        await page.goto('https://httpbin.org/get')
        print(page.content())
        await browser.close()

    if __name__ == '__main__':
        asyncio.run(main())

def proxy_socks():
    proxy = '127.0.0.1:7891'

    async def main():
        browser = await launch({'args': ['--proxy-server=socks5://' + proxy], 'headless': False})
        page = await browser.newPage()
        await page.goto('https://httpbin.org/get')
        print(page.content())
        await browser.close()

    if __name__ == '__main__':
        asyncio.run(main())
