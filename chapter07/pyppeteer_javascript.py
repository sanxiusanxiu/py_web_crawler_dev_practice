import asyncio
from pyppeteer import launch

async def main():
    # 解决 浏览器窗口很大，内容显示却很小 的问题
    browser = await launch(headless=False,
                           args=['--window-size=1280,720'], defaultViewport={"width": 1280,"height": 720})
    page = await browser.newPage()
    await page.goto('https://spa2.scrape.center/')
    await page.waitForSelector('.item .name', timeout=3000)
    await asyncio.sleep(2)
    await page.screenshot(path='pyppeteer_javascript.png')
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
    print(dimensions)
    await asyncio.sleep(1)
    await browser.close()

asyncio.run(main())

"""
除了 waitForSelector，还有其他的一些等待方法

waitForFunction：等待某个 JavaScript 方法执行完毕或返回结果
waitForNavigation：等待页面跳转，如果没加载出来，就报错
waitForRequest：等待某个特定的请求发出
waitForResponse：等待某个特定请求对应的响应
waitFor：通用的等待方法
waitForXPath：等待符合 XPath 的节点加载出来
"""
