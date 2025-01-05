from selenium import webdriver

path = './phantomjs.exe'

# 因版本更新，已经无法使用 PhantomJS
browser = webdriver.PhantomJS(path)

url = 'https://www.baidu.com'
browser.get(url)

print(browser.current_url)
