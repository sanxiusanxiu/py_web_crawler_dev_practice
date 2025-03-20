import asyncio
from pyppeteer import launch

async def main():
    browser = await launch(headless=False, args=['--start-maximized',])
    # 无效的
    context = await browser.createIncognitoBrowserContext()
    page = await context.newPage()
    await page.goto('https://scrape.center/')
    await asyncio.sleep(20)
    await context.close()

asyncio.get_event_loop().run_until_complete(main())
