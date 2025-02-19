from playwright.sync_api import sync_playwright

def event_listening_simple():
    def on_response(response):
        print(f'状态码 {response.status}: {response.url}')

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()
        # 监听response事件
        page.on('response', on_response)
        page.goto('https://spa6.scrape.center/')
        page.wait_for_load_state('networkidle')
        browser.close()

def event_listening_base():
    def on_response(response):
        # 截获Ajax请求，拿到最后的响应结果
        if '/api/movie/' in response.url and response.status == 200:
            print(response.json())

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()
        # 监听response事件
        page.on('response', on_response)
        page.goto('https://spa6.scrape.center/')
        page.wait_for_load_state('networkidle')
        browser.close()

event_listening_base()
