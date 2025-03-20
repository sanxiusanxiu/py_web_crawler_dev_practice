import asyncio
from pyppeteer import launch

def shield():
    async def main():
        browser = await launch(headless=False)
        page = await browser.newPage()
        await page.goto('https://antispider1.scrape.center/')
        await asyncio.sleep(5)
        await browser.close()

    asyncio.run(main())

def antishield():
    async def main():
        browser = await launch(headless=False)
        page = await browser.newPage()
        # evaluateOnNewDocument 是每次加载网页时执行命令的语句，这里用来隐藏 webdriver 属性
        await page.evaluateOnNewDocument('Object.defineProperty(navigator, "webdriver", {get: () => undefined})')
        await page.goto('https://antispider1.scrape.center/')
        await asyncio.sleep(5)
        await browser.close()

    asyncio.run(main())

# shield()
antishield()
