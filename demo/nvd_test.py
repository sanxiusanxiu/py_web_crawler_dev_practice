import requests
from lxml import etree
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
}

# https://nvd.nist.gov/vuln/detail/CVE-2024-27923
# https://nvd.nist.gov/vuln/detail/CVE-2024-27923#vulnDescriptionTitle
# url = 'https://nvd.nist.gov'
url = 'https://nvd.nist.gov/vuln/data-feeds'
response = requests.get(url, headers=headers)

if response.status_code == 200:
    print('-- 首页请求成功 --')
    print(response.text)
