from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://spa6.scrape.center/')
    page.wait_for_load_state('networkidle')

    # 页面点击
    # page.click(selector, **kwargs)

    # 文本输入
    # page.fill(selector, value, **kwargs)

    # 获取节点属性
    # page.get_attribute(selector, name, **kwargs)

    # 获取多个节点
    # page.query_selector_all(selector)

    # 获取单个节点
    # page.query_selector(selector)

    browser.close()
