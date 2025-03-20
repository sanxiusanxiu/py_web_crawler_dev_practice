import asyncio
from pyppeteer import launch
from pyquery import PyQuery as pq

async def main():
    browser = await launch()
    page = await browser.newPage()
    await page.goto('https://spa2.scrape.center/')
    await page.waitForSelector('.item .name')
    # J 方法等价于 querySelector 方法
    j_result = await page.J('.item .name')
    pq_result = await page.querySelector('.item .name')
    # JJ 方法等价于 querySelectorAll 方法
    jj_result = await page.JJ('.item .name')
    pq_all_result = await page.querySelectorAll('.item .name')
    print('j_result:', j_result)
    print('pq_result:', pq_result)
    print('jj_result:', jj_result)
    print('pq_all_result:', pq_all_result)
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())
