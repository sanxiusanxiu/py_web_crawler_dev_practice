from urllib.parse import urlencode

# 声明字典保存参数
params = {
    'name': 'germey',
    'age': 22
}
base_url = 'https://www.baidu.com?'
# 序列化为GET请求
url = base_url + urlencode(params)
print(url)
