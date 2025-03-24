import requests

url = 'https://www.httpbin.org/ip'

# 代理信息
proxy_host = 'tps163.kdlapi.com'
proxy_port = '12345'
proxy_username = ''
proxy_password = ''

proxy = f'https://{proxy_username}:{proxy_password}@{proxy_host}:{proxy_port}'
proxys = {
    'http': proxy,
    'https': proxy,
}

response = requests.get(url, proxies=proxys)
print(response.text)
