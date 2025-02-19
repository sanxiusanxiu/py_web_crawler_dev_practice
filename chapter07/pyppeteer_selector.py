import asyncio
from pyppeteer import launch
from pyquery import PyQuery as pq

async def main():
    browser = await launch()
    page = await browser.newPage()
    await page.goto('https://spa2.scrape.center/')
    await page.waitForSelector('.item .name')
    # J方法等价于querySelector方法
    j_result = await page.J('.item .name')
    pq_result = await page.querySelector('.item .name')
    # JJ方法等价于querySelectorAll方法
    jj_result = await page.JJ('.item .name')
    pq_all_result = await page.querySelectorAll('.item .name')
    print('j_result:', j_result)
    print('pq_result:', pq_result)
    print('jj_result:', jj_result)
    print('pq_all_result:', pq_all_result)
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())
