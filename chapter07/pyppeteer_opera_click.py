import asyncio
from pyppeteer import launch

async def main():
    # 解决 浏览器窗口很大，内容显示却很小 的问题
    browser = await launch(headless=False,
                           args=['--window-size=1280,720'], defaultViewport={"width": 1280,"height": 720})
    page = await browser.newPage()
    await page.goto('https://spa2.scrape.center/')
    await page.waitForSelector('.item .name', timeout=3000)
    # button 表示鼠标按钮，clickCount 表示点击次数，一般有单击或者双击，delay 表示延迟点击，单位毫秒
    await page.click('.item .name', options={'button': 'left', 'clickCount': 1, 'delay': 2000})
    await asyncio.sleep(6)
    await browser.close()

asyncio.run(main())
