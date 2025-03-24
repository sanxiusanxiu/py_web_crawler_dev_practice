import requests

# 快代理的 API 链接
PROXY_API = ''

def get_proxys():
    # 得到代理列表
    response = requests.get(PROXY_API)
    return response.text.split('\n')

def test_proxy():
    proxys = get_proxys()
    for proxy in proxys:
        proxy = proxy.split()
        print(f'正在使用代理 {proxy}')
        try:
            response = requests.get('https://www.httpbin.org/ip', proxies={
                'https': 'https://' + proxy[0]})
            print(response.text)
        except requests.exceptions.ConnectionError:
            print(f'代理 {proxy} 出问题啦！')

if __name__ == '__main__':
    test_proxy()

"""
正在使用代理 ['111.72.200.179:21978']
{
  "origin": "111.72.200.179"
}

正在使用代理 ['58.19.54.132:20968']

正在使用代理 ['183.130.235.88:16870']
{
  "origin": "183.130.235.88"
}

正在使用代理 ['221.234.30.64:20919']
{
  "origin": "221.234.30.64"
}

正在使用代理 ['58.19.54.142:16650']

正在使用代理 ['182.106.136.217:20846']

正在使用代理 ['182.106.136.217:20783']

正在使用代理 ['112.29.133.160:12314']

正在使用代理 ['182.106.136.217:20412']

正在使用代理 ['125.117.211.133:21739']
{
  "origin": "125.117.211.133"
}
"""