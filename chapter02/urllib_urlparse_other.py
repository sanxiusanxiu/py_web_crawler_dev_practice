from urllib.parse import urlparse

"""
urllib.parse.urlparse(urlstring, scheme='', allow_fragments=True)

urlstring 参数，待解析的 URL
scheme 参数，代表协议，如果 URL 链接里标明协议了，该参数不会生效
allow_fragments 参数，是否忽略 fragment 
"""


def urlparse_scheme():
    result = urlparse('www.baidu.com/index.html;user?id=5#comment', scheme='https')
    # ParseResult(scheme='https', netloc='', path='www.baidu.com/index.html', params='user', query='id=5', fragment='comment')
    print(result)


def urlparse_scheme2():
    result = urlparse('http://www.baidu.com/index.html;user?id=5#comment', scheme='https')
    # ParseResult(scheme='http', netloc='www.baidu.com', path='/index.html', params='user', query='id=5', fragment='comment')
    print(result)


def urlparse_allow_fragments():
    result = urlparse('http://www.baidu.com/index.html;user?id=5#comment', allow_fragments=False)
    # ParseResult(
    # scheme='http', netloc='www.baidu.com', path='/index.html', params='user', query='id=5#comment', fragment=''
    # )
    print(result)


def urlparse_allow_fragments2():
    result = urlparse('http://www.baidu.com/index.html#comment', allow_fragments=False)
    # ParseResult(
    # scheme='http', netloc='www.baidu.com', path='/index.html#comment', params='', query='', fragment=''
    # )
    print(result)


def urlparse_get_result():
    result = urlparse('http://www.baidu.com/index.html#comment', allow_fragments=False)
    # ParseResult 是一个元组，可以使用索引获取内容，也可以使用属性名获取内容
    print(result.scheme, result[0], result.netloc, result[1], sep='\n')


urlparse_scheme()
urlparse_scheme2()
urlparse_allow_fragments()
urlparse_allow_fragments2()
urlparse_get_result()
