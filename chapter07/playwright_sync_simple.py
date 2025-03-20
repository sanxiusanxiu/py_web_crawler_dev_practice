from playwright.sync_api import sync_playwright

# 同步模式
with sync_playwright() as playwright:
    # playwright 调用一个浏览器上下文管理器，然后依次调用 chromium、firefox、webkit
    for browser_type in [playwright.chromium, playwright.firefox, playwright.webkit]:
        # 启动并设置为无头模式
        browser = browser_type.launch(headless=False)
        page = browser.new_page()
        page.goto('https://www.baidu.com')
        page.screenshot(path=f'playwright_simple_{browser_type.name}.png')
        print(page.title())
        browser.close()
