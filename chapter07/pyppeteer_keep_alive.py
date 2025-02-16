import asyncio
from pyppeteer import launch

async def main():
    browser = await launch(headless=False, userDataDir='./userdata')
    page = await browser.newPage()
    await page.goto('https://scrape.center/')
    await asyncio.sleep(20)

asyncio.get_event_loop().run_until_complete(main())
