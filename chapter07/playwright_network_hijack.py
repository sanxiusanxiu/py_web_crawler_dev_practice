import re

from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    # 取消本次请求
    def cancel_request(route, request):
        route.abort()

    # 取消图片的加载，因为我们不关心图片如何，而需要的是URL，这样可以提速
    page.route(re.compile(r'(\.png)|(\.jpg)'), cancel_request)
    page.goto('https://spa6.scrape.center/')
    page.wait_for_load_state('networkidle')
    page.screenshot(path='playwright_hijack_no_picture.png')
    browser.close()
