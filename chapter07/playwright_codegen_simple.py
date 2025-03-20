import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.firefox.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://scrape.center/")
    with page.expect_popup() as page1_info:
        page.get_by_role("link", name="SSR 网站 ssr2 电影数据网站，无反爬，无").click()
    page1 = page1_info.value
    page1.get_by_role("link", name="这个杀手不太冷 - Léon").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
