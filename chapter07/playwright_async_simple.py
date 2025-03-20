import asyncio
from playwright.async_api import async_playwright

# 异步模式
async def main():
    async with async_playwright() as playwright:
        for browser_type in [playwright.chromium, playwright.firefox, playwright.webkit]:
            browser = await browser_type.launch()
            page = await browser.new_page()
            await page.goto('https://www.baidu.com')
            await page.screenshot(path=f'playwright_simple_{browser_type.name}.png')
            print(await page.title())
            await browser.close()

asyncio.run(main())
