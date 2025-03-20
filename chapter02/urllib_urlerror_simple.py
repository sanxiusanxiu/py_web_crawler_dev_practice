from urllib import request, error

try:
    response = request.urlopen('https://cuiqingcai.com/404')
except error.URLError as e:
    # 打印错误原因  # Not Found
    print(e.reason)
