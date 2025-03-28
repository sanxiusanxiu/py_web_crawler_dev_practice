from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # 模拟打开 iPhone 12 Pro Max 上的 Safari 浏览器
    iphone_12_pro_max = p.devices['iPhone 12 Pro Max']
    browser = p.webkit.launch(headless=False)
    context = browser.new_context(
        **iphone_12_pro_max,
        locale='zh-CN'
    )
    page = context.new_page()
    page.goto('https://www.whatismybrowser.com/')
    # networkidle 表示网络空闲状态
    page.wait_for_load_state(state='networkidle')
    page.screenshot(path='playwright_iphone.png')
    browser.close()
