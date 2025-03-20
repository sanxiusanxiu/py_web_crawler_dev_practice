import requests


def requests_get_base():
    r = requests.get('https://httpbin.org/get')
    print(r.text)
    """
    运行结果如下，其中包含请求头、URL、IP 等信息
    {
      "args": {}, 
      "headers": {
        "Accept": "*/*", 
        "Accept-Encoding": "gzip, deflate", 
        "Host": "httpbin.org", 
        "User-Agent": "python-requests/2.17.3", 
        "X-Amzn-Trace-Id": "Root=1-6741831c-1cd121d078ff617a115b76c8"
      }, 
      "origin": "223.88.17.244", 
      "url": "https://httpbin.org/get"
    }
    """


def requests_get_params():
    # 对于 GET 请求，利用 params 参数附带额外的信息
    data = {
        'name': 'David',
        'age': 22
    }
    r = requests.get('https://httpbin.org/get', params=data)
    # 另外，网页的返回类型实际上是 str 类型、 JSON 格式
    # print(r.text)
    # 如果想直接解析需要调用 json() ，将 JSON 转化为字典
    print(r.json())
    """
    运行结果如下，请求链接自动被构建成了 https://httpbin.org/get?name=germey&age=22 
    {
      "args": {
        "age": "22", 
        "name": "David"
      }, 
      "headers": {
        "Accept": "*/*", 
        "Accept-Encoding": "gzip, deflate", 
        "Host": "httpbin.org", 
        "User-Agent": "python-requests/2.17.3", 
        "X-Amzn-Trace-Id": "Root=1-67418464-61d8549f19ac4bf919063eb0"
      }, 
      "origin": "223.88.17.244", 
      "url": "https://httpbin.org/get?name=germey&age=22"
    }
    """


def requests_get_headers():
    import re

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHML, like Gecko) '
                      'Chrome/52.0.2743.116 Safari/537.36',
    }
    # 请求普通网页，获得相应内容
    r = requests.get('https://www.zhihu.com/explore', headers=headers)
    # 20241123 修改正则
    # pattern = re.compile('explore-feed.*?question_link.*?>(.*?)</a>', re.S)
    pattern = re.compile('ExploreSpecialCard-contentItem.*?>(.*?)</a>', re.S)
    titles = re.findall(pattern, r.text)
    print(titles)


def requests_get_picture():
    # 抓取二进制数据 # 需要添加 headers
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
    }
    r = requests.get('https://github.com/favicon.ico', headers=headers)
    print(r.text)
    # 保存图片
    with open('favicon.ico', 'wb') as f:
        f.write(r.content)

# requests_get_base()
# requests_get_params()
# requests_get_headers()
# requests_get_picture()
