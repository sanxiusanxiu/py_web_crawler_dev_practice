from playwright.sync_api import sync_playwright

def proxy_simple():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(proxy={
            'server': 'http://127.0.0.1:7890',
            'username': 'admin',
            'password': '<PASSWORD>',
        })
        page = browser.new_page()
        page.goto('https://httpbin.org/get')
        print(page.content())
        browser.close()

def proxy_socks():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(proxy={
            'server': 'socks5://127.0.0.1:7891',
        })
        page = browser.new_page()
        page.goto('https://httpbin.org/get')
        print(page.content())
        browser.close()