import asyncio
from pyppeteer import launch

async def main():
    browser = await launch(headless=False)
    page = await browser.newPage()
    await page.goto('https://www.baidu.com/')
    page = await browser.newPage()
    await page.goto('https://www.bing.com/')
    pages = await browser.pages()
    print('页面：', pages)
    page_new = pages[1]
    await page_new.bringToFront()
    await asyncio.sleep(10)

asyncio.get_event_loop().run_until_complete(main())
