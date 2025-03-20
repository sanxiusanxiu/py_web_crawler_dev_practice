import requests


def requests_post_base():
    data = {'name': 'Sarah', 'age': 22}
    r = requests.post('https://httpbin.org/post', data=data)
    print(r.text)
    """
    运行结果如下，其中包含请求头、URL、IP 等信息
    {
      "args": {}, 
      "data": "", 
      "files": {}, 
      "form": {
        "age": "22", 
        "name": "Sarah"
      }, 
      "headers": {
        "Accept": "*/*", 
        "Accept-Encoding": "gzip, deflate", 
        "Content-Length": "18", 
        "Content-Type": "application/x-www-form-urlencoded", 
        "Host": "httpbin.org", 
        "User-Agent": "python-requests/2.17.3", 
        "X-Amzn-Trace-Id": "Root=1-67419824-7108a0033991426e5e23ad4f"
      }, 
      "json": null, 
      "origin": "223.88.17.244", 
      "url": "https://httpbin.org/post"
    }
    """

requests_post_base()
