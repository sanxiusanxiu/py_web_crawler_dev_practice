import urllib.request
import urllib.parse
import urllib.error


def urlopen_data():
    data = bytes(urllib.parse.urlencode({'word': 'hello'}), encoding='utf8')
    # https://httpbin.org/post 是测试POST请求的链接
    response = urllib.request.urlopen('https://httpbin.org/post', data=data)

    # 从返回的结果中可以看到 from ，这表明是模拟了表单提交的方式，以POST方式传输数据
    print(response.read())


def urlopen_timeout():
    response = urllib.request.urlopen('https://httpbin.org/get', timeout=1)

    # 因此，可以通过设置超时时间来控制一个页面如果长时间未响应，就跳过它的抓取
    print(response.read())


def urlopen_timeout2():
    import socket

    try:
        response = urllib.request.urlopen('https://httpbin.org/get', timeout=0.1)
    except urllib.error.URLError as e:
        if isinstance(e.reason, socket.timeout):
            print('time out.')


'''
urllib.request.urlopen(url, data=None, [timeout, ]*, cafile=None, capath=None, cadefault=False, context=None)

data 参数如果是字节流编码格式时（bytes类型）需要使用bytes()方法转化，另外添加这个参数之后就不再是GET方式请求了，而是POST方式
timeout 参数用来设置超时时间（秒），支持HTTP、HTTPS、FTP请求
cafile 参数，用于指定CA证书，这在请求HTTPS链接时有用
capath 参数，用于指定CA证书的路径
cadefault 参数已弃用
context 参数必须是 ssl.SSLContext 类型，用来指定SSL设置
'''

# urlopen_data()
# urlopen_timeout()
# urlopen_timeout2()