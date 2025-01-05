from urllib.parse import urlparse


def urlparse_scheme():
    result = urlparse('www.baidu.com/index.html;user?id=5#comment', scheme='https')
    print(result)


def urlparse_scheme2():
    result = urlparse('http://www.baidu.com/index.html;user?id=5#comment', scheme='https')
    print(result)


def urlparse_allow_fragments():
    result = urlparse('http://www.baidu.com/index.html;user?id=5#comment', allow_fragments=False)
    # ParseResult(
    # scheme='http', netloc='www.baidu.com', path='/index.html', params='user', query='id=5#comment', fragment=''
    # )
    print(result)


def urlparse_allow_fragments2():
    result = urlparse('http://www.baidu.com/index.html#comment', allow_fragments=False)
    # ParseResult(scheme='http', netloc='www.baidu.com', path='/index.html#comment', params='', query='', fragment='')
    print(result)


def urlparse_result():
    result = urlparse('http://www.baidu.com/index.html#comment', allow_fragments=False)
    # ParseResult 是一个元组，可以使用索引获取内容，或者使用属性名获取内容
    print(result.scheme, result[0], result.netloc, result[1], sep='\n')


'''
urllib.parse.urlparse(urlstring, scheme='', allow_fragments=True)

urlstring 待解析的URL
scheme 参数代表协议，如果URL链接里标明协议了，该参数不会生效
allow_fragments 是否忽略 fragment 
'''

# urlparse_scheme()
# urlparse_scheme2()
# urlparse_allow_fragments()
# urlparse_allow_fragments2()
urlparse_result()
