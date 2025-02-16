import asyncio
from pyppeteer import launch

async def main():
    browser = await launch(headless=False, args=[
        # 启动浏览器时最大化窗口
        '--start-maximized',
        # 用户代理
        '--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        # 隐藏提示栏
        '--disable-infobars',
        # 取消沙盒模式
        '--no-sandbox',
    ])
    context = await browser.createIncognitoBrowserContext()
    page = await context.newPage()
    await page.goto('https://scrape.center/')
    await asyncio.sleep(20)
    await context.close()

asyncio.get_event_loop().run_until_complete(main())
