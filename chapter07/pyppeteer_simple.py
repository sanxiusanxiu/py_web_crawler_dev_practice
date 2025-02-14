import asyncio
import os

from pyppeteer import launch
from pyquery import PyQuery as pq

# 指定Chromium浏览器的路径
executable_path = './mini_installer.exe'
# 设置环境变量以阻止自动下载Chromium
os.environ['PYPPETEER_CHROMIUM_REVISION'] = 'None'

async def main():
    # 启动浏览器
    browser = await launch(executable_path=executable_path)
    # 启动一个新的选项卡
    page = await browser.newPage()
    # 加载测试网站
    await page.goto('https://spa2.scrape.center/')
    # 传入选择器
    await page.waitForSelector('.item .name')
    # 获取JS渲染后的页面
    doc = pq(await page.content())
    # 使用pyquery解析并提取页面上的电影名称
    names = [item.text() for item in doc('.item .name').items()]
    print('电影名称：', names)
    await browser.close()

asyncio.run(main())
