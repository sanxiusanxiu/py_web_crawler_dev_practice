import asyncio
from pyppeteer import launch

async def main():
    # 启动浏览器
    browser = await launch()
    # 启动一个新的选项卡
    page = await browser.newPage()
    # 设置窗口大小
    await page.setViewport({'width': 1920, 'height': 1080})
    await page.goto('https://spa2.scrape.center/')
    await page.waitForSelector('.item .name')
    await asyncio.sleep(2)
    # 保存截图
    await page.screenshot({'path': 'pyppeteer_base.png'})
    # 执行 JavaScript，返回页面的宽、高、像素大小比率
    dimensions = await page.evaluate('''
    () => {
        return {
            width: document.documentElement.clientWidth,
            height: document.documentElement.clientHeight,
            deviceScaleFactor: window.devicePixelRatio,
        }
    }
    ''')

    print(dimensions)  # dimensions  n.维度，层面
    await browser.close()

asyncio.run(main())
