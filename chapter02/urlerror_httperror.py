from urllib import request, error

# 因为 URLError 是 HTTPError 的父类，所以可以先捕获子类的错误，再捕获父类的错误
try:
    response = request.urlopen('https://cuiqingcai.com/index.htm')
except error.HTTPError as e:
    print(e.reason, e.code, e.headers)
except error.URLError as e:
    print(e.reason)
else:
    print('请求成功！')
