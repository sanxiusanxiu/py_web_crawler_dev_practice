import requests
from lxml import etree
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
}

# https://nvd.nist.gov/vuln/detail/CVE-2024-27923
# https://nvd.nist.gov/vuln/detail/CVE-2024-27923#vulnDescriptionTitle
url = 'https://nvd.nist.gov'
response = requests.get(url, headers=headers)

if response.status_code == 200:
    print('-- 首页请求成功 --')
    html_content = response.content
    html = etree.HTML(html_content)

detail_list = html.xpath('//*[@id="latestVulns"]/li/div/p/a/@href')
# print(detail_list)

for item in detail_list:
    detail_url = url + item

    file_name = item.split('#')[0].split('/')[-1]
    time.sleep(7)

    detail_response = requests.get(detail_url, headers=headers)
    if detail_response.status_code == 200:
        print(f'-- {detail_url} 请求成功 --')
        detail_content = detail_response.content
        detail_html = etree.HTML(detail_content)
        with open(f'./vul/{file_name}.html', 'w', encoding='utf-8') as file:
            file.write(detail_html.text)
            print(f'-- {file_name} 保存成功 --')

