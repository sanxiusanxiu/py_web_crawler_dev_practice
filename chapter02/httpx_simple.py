
def requests_get_http2():
    import requests

    url = 'https://spa16.scrape.center/'
    response = requests.get(url)
    print(response.text)

def httpx_get():
    import httpx
    # 开启HTTP2.0
    client = httpx.Client(http2=True)
    response = client.get(url='https://spa16.scrape.center/')
    print(response.text)

def httpx_client():
    import httpx
    # 官方推荐使用with as语句
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
# httpx_get()
# httpx_client()
httpx_client_paras()
