import asyncio
from pyppeteer import launch

async def main():
    browser = await launch(headless=False, args=[
        '--disable-infobars',
        '--disable-blink-features=AutomationControlled'
    ])
    await asyncio.sleep(30)
    await browser.close()

asyncio.run(main())
