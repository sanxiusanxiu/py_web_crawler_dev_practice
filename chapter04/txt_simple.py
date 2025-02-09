import requests
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
}

url = 'https://www.zhihu.com/explore'
response = requests.get(url, headers=headers)
if response.status_code == 200:
    html = etree.HTML(response.text)
    # 取出 a 标签下的所有文本
    result = html.xpath('//a//text()')
    for item in result:
        # 简单过滤一下标题内容，这里认为真正的标题文字较长
        if len(item) > 6:
            with open('txt_simple.txt', 'a', encoding='utf-8') as file:
                file.write(item)
                file.write('\n')
