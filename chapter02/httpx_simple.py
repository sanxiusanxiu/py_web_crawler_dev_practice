
def requests_get_http2():
    import requests

    url = 'https://spa16.scrape.center/'
    response = requests.get(url)
    # http.client.RemoteDisconnected: Remote end closed connection without response
    print(response.text)

def httpx_simple():
    import httpx

    response = httpx.get(url='https://www.httpbin.org/get')
    print(response.status_code)
    print(response.headers)
    # 可以注意一下 User-Agent 字段的内容  "User-Agent": "python-httpx/0.28.1",
    print(response.text)

def httpx_get():
    import httpx

    # 默认是 HTTP1.0，需要手动开启 HTTP2.0
    client = httpx.Client(http2=True)
    response = client.get(url='https://spa16.scrape.center/')
    print(response.text)

def httpx_client():
    import httpx

    # 官方推荐使用 with as 语句
    with httpx.Client() as client:
        response = client.get(url='https://www.httpbin.org/get')
        print(response)

def httpx_client_paras():
    import httpx

    url = 'https://www.httpbin.org/headers'
    headers = {'User-Agent': 'my-app/0.0.1'}

    with httpx.Client(headers=headers) as client:
        r = client.get(url)
        print(r.json()['headers']['User-Agent'])

# requests_get_http2()
# httpx_simple()
# httpx_get()
# httpx_client()
# httpx_client_paras()
