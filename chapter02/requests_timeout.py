import requests

# timeout 是请求（请求分为连接和读取两个阶段）的总和
r = requests.get('https://www.taobao.com', timeout=1)
print(r.status_code)

# 分别指定两个阶段的时间
# r = requests.get('https://www.taobao.com', timeout=(5, 11))

# 设置永久等待
# r = requests.get('https://www.taobao.com', timeout=None)
