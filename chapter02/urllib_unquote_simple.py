from urllib.parse import unquote

url = 'https://www.baidu.com/s?wd=%E5%A3%81%E7%BA%B8'
# https://www.baidu.com/s?wd=壁纸
print(unquote(url))
