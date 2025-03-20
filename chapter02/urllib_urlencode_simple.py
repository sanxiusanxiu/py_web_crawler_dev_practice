from urllib.parse import urlencode

# 声明字典保存参数
params = {
    'name': 'Smith',
    'age': 22
}
base_url = 'https://www.baidu.com?'

# 序列化为 GET 请求
url = base_url + urlencode(params)
# https://www.baidu.com?name=Smith&age=22
print(url)
