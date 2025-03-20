import time

from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    # 指定响应文件
    def modify_response(route, request):
        route.fulfill(path='playwright_custom_response.html')

    page.route('**/*', modify_response)
    page.goto('https://spa6.scrape.center/')
    page.pause()
    browser.close()
