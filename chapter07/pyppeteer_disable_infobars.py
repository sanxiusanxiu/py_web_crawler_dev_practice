import asyncio
from pyppeteer import launch

async def main():
    # browser = await launch(headless=False, args=[
    #         '--disable-infobars',
    #         '--disable-blink-features=AutomationControlled'
    #     ])
    # https://www.jianshu.com/p/ef86d9963009
    browser = await launch(headless=False, ignoreDefaultArgs=['--enable-automation'])
    page = await browser.newPage()
    await page.goto('https://www.baidu.com')
    await asyncio.sleep(30)
    await browser.close()

asyncio.run(main())
