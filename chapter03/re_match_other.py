import re


def re_match_base():
    content = 'Hello 123 4567 World_This is a Regex Demo.'
    print(len(content))
    result = re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}', content)
    print(result)
    # 输出匹配到的内容
    print(result.group())
    # 输出匹配的范围
    print(result.span())


def re_match2():
    # 如果想从字符串中提取一部分内容，可以使用括号将想提取的子字符串括起来 # 匹配目标
    content = 'Hello 1234567 World_This is a Regex Demo.'
    print(len(content))
    result = re.match('^Hello\s(\d+)\sWorld', content)
    # 输出匹配到的内容
    print(result.group())
    # 输出第一个被括号包围的匹配结果
    print(result.group(1))
    print(result.span())


# 通用匹配
def re_match3():
    content = 'Hello 123 4567 World_This is a Regex Demo'
    print(len(content))
    result = re.match('^Hello.*Demo$', content)
    print(result)
    print(result.group())
    print(result.span())


# 贪婪与非贪婪
def re_match4():
    content = 'Hello 1234567 World_This is a Regex Demo'
    # 贪婪模式下.*会尽可能多的匹配字符
    result = re.match('^He.*(\d+).*Demo$', content)
    # 贪婪模式下.*?则是尽可能少的匹配字符
    result2 = re.match('^He.*?(\d+).*Demo$', content)
    print(result)
    print(result.group(1))
    # 字符串中间应尽量使用非贪婪匹配，以免出现匹配结果缺失的情况
    print(result2)
    print(result2.group(1))


# 需要注意一点，如果匹配的结果在字符串结尾，非贪婪匹配可能匹配不到内容，因为非贪婪是尽可能少的匹配
def re_match5():
    content = 'https://weibo.com/comment/KEraCN'
    result1 = re.match('https.*?comment/(.*?)', content)
    result2 = re.match('https.*?comment/(.*)', content)
    print('结果1：', result1.group(1))
    print('结果2：', result2.group(1))


# 修饰符，常见的还有re.I，re.L，re.M，re.S，re.U，re.X
def re_match6():
    content = '''Hello 1234567 World_This 
    is a Regex Demo'''
    # re.S使.匹配包括换行符在内的所有字符
    result = re.match('^He.*?(\d+).*?Demo$', content, re.S)
    # 因为HTML中经常会有换行，所以re.S在网页匹配中很常见
    print(result.group(1))


# 转义匹配，主要应对目标字符串里包含特殊字符的情况
def re_match7():
    content = '(百度)www.baidu.com'
    result = re.match('\(百度\)www\.baidu\.com', content)
    print(result)


# re_match_base()
# re_match2()
# re_match3()
# re_match4()
re_match5()
# re_match6()
# re_match7()
