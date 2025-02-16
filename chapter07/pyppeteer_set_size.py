import asyncio
from pyppeteer import launch

width = 1920
height = 1080

async def main():
    browser = await launch(headless=False, args=[f'--window-size={width}, {height}'])
    page = await browser.newPage()
    await page.setViewport({'width': width, 'height': height})
    await page.evaluateOnNewDocument('Object.defineProperty(navigator, "webdriver", {get: () => undefined})')
    await page.goto('https://antispider1.scrape.center/')
    await asyncio.sleep(5)
    await browser.close()

asyncio.run(main())
