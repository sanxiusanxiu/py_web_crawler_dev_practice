from urllib import request, error

try:
    response = request.urlopen('https://cuiqingcai.com/index.htm')
except error.URLError as e:
    # 打印错误原因
    print(e.reason)
