import asyncio
from pyppeteer import launch

async def main():
    browser = await launch(headless=False)
    await asyncio.sleep(300)
    await browser.close()

asyncio.run(main())
