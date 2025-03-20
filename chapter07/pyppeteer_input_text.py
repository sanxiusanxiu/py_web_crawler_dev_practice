import asyncio
from pyppeteer import launch

async def main():
    # 解决 浏览器窗口很大，内容显示却很小 的问题
    browser = await launch(headless=False,
                           args=['--window-size=1280,720'], defaultViewport={"width": 1280,"height": 720})
    page = await browser.newPage()
    await page.goto('https://www.baidu.com')
    #
    await page.type('#kw', 'pyppeteer')
    await asyncio.sleep(6)
    await browser.close()

asyncio.run(main())
