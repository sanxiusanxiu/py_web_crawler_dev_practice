import requests
from urllib.parse import urljoin


def login2_pre():
    base_url = 'https://login2.scrape.center/'
    login_url = urljoin(base_url, '/login')
    index_url = urljoin(base_url, '/page/1')

    username = 'admin'
    password = 'admin'

    response_login = requests.post(login_url, data={'username': username, 'password': password})
    response_index = requests.get(index_url)

    print('状态码：', response_index.status_code)
    print('URL: ', response_index.url)


def login2_simple():
    base_url = 'https://login2.scrape.center/'
    login_url = urljoin(base_url, '/login')
    index_url = urljoin(base_url, '/page/1')

    username = 'admin'
    password = 'admin'
    # allow_redirects=False 设置 requests 不自动处理重定向
    response_login = requests.post(login_url, data={'username': username, 'password': password},
                                   allow_redirects=False)
    cookies = response_login.cookies
    print('Cookies: ', cookies)
    response_index = requests.get(index_url, cookies=cookies)

    print('状态码：', response_index.status_code)
    print('URL: ', response_index.url)


def login2_session():
    base_url = 'https://login2.scrape.center/'
    login_url = urljoin(base_url, '/login')
    index_url = urljoin(base_url, '/page/1')
    username = 'admin'
    password = 'admin'
    session = requests.session()
    #
    response_login = requests.post(login_url, data={'username': username, 'password': password})
    cookies = session.cookies
    print('Cookies: ', cookies)
    response_index = session.get(index_url)
    print('状态码：', response_index.status_code)
    print('URL: ', response_index.url)


# login2_pre()
# login2_simple()
# login2_session()
