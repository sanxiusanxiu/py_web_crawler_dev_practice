import asyncio
from pyppeteer import launch

async def main():
    browser = await launch(devtools=True)
    page = await browser.newPage()
    await page.goto('https://www.baidu.com')
    await asyncio.sleep(100)
    await browser.close()

asyncio.run(main())
