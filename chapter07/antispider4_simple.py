
def anti4_selenium():
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.support.wait import WebDriverWait
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.chrome.service import Service
    from pyquery import PyQuery as pq

    url = 'https://antispider4.scrape.center/'
    chrome_driver_path = 'chromedriver.exe'
    time_out = 30

    chrome_options = Options()
    service = Service(executable_path=chrome_driver_path)
    browser = webdriver.Chrome(service=service, options=chrome_options)

    browser.get(url)
    WebDriverWait(browser, time_out).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.item')))
    # 页面源代码
    html = browser.page_source
    doc = pq(html)
    items = doc('.item')
    for item in items.items():
        name = item('.name').text()
        categories = [o.text() for o in item('.categories button').items()]
        score = item('.score').text()
        print(f'电影名称：{name} 类别：{categories} 评分：{score}')

    browser.close()

def anti4_requests():
    import re
    import requests

    url = 'https://antispider4.scrape.center/css/app.654ba59e.css'

    response = requests.get(url)
    # 使用正则提取映射，例如 .icon-281:before { content: "8" } 提取到的是 281 和 8
    pattern = re.compile(r'.icon-(.*?):before\{content:"(.*?)"\}')
    results = re.findall(pattern, response.text)
    icon_map = {item[0]: item[1] for item in results}
    print(icon_map['281'])

# anti4_selenium()
anti4_requests()
