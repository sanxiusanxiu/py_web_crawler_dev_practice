import urllib.request
import gzip
from io import BytesIO

# 向Python官网发送请求
response = urllib.request.urlopen('https://www.python.org')

# 输出响应的类型
print('响应的类型：', type(response))

# 读取返回的网页内容
# print(response.read().decode('utf-8'))
# 20241105  原因：python.org的网站使用了gzip压缩来传输内容
# UnicodeDecodeError: 'utf-8' codec can't decode byte 0x8b in position 1: invalid start byte

content = response.read()
# 检查内容是否为gzip压缩
if response.info().get('Content-Encoding') == 'gzip':
    # 如果是gzip压缩，则先解压
    buf = BytesIO(content)
    f = gzip.GzipFile(fileobj=buf)
    content = f.read()

# 将内容解码为字符串输出
content = content.decode('utf-8')
# print(content)

# 打印响应的状态码
print(response.status)
# 打印响应的头信息
print(response.getheaders())
