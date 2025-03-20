import asyncio
from pyppeteer import launch
from pyquery import PyQuery as pq

async def main():
    # 启动浏览器
    browser = await launch()
    # 启动一个新的选项卡
    page = await browser.newPage()
    # 加载测试网站
    await page.goto('https://spa2.scrape.center/')
    # 传入选择器
    await page.waitForSelector('.item .name')
    # 获取 JavaScript 渲染后的页面
    doc = pq(await page.content())
    # 使用 pyquery 解析并提取页面上的电影名称
    names = [item.text() for item in doc('.item .name').items()]
    print('电影名称：', names)
    await browser.close()

asyncio.run(main())
