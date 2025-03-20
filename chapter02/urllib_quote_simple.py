from urllib.parse import quote

keyword = '壁纸'
url = 'https://www.baidu.com/s?wd=' + quote(keyword)
# https://www.baidu.com/s?wd=%E5%A3%81%E7%BA%B8
print(url)
