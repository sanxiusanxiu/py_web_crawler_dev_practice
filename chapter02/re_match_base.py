import re


# 匹配目标
def re_match_target():
    # 如果想从字符串中提取一部分内容，可以使用括号将想提取的子字符串括起来
    content = 'Hello 1234567 World_This is a Regex Demo.'
    print(len(content))

    result = re.match(r'^Hello\s(\d+)\sWorld', content)
    # Hello 1234567 World
    print(result.group())
    # 输出第一个被括号包围的匹配结果 1234567
    print(result.group(1))
    # (0, 19)
    print(result.span())


# 通用匹配
def re_match_universal():
    content = 'Hello 123 4567 World_This is a Regex Demo'
    print(len(content))

    result = re.match(r'^Hello.*Demo$', content)
    # <re.Match object; span=(0, 41), match='Hello 123 4567 World_This is a Regex Demo'>
    print(result)
    # Hello 123 4567 World_This is a Regex Demo
    print(result.group())
    # (0, 41)
    print(result.span())


# 贪婪匹配
def re_match_greed():
    content = 'Hello 1234567 World_This is a Regex Demo'
    # 贪婪模式下 .* 会尽可能多的匹配字符
    result = re.match(r'^He.*(\d+).*Demo$', content)
    # <re.Match object; span=(0, 40), match='Hello 1234567 World_This is a Regex Demo'>
    print(result)
    # 7 ，这里只有 7 是因为 .* 把 123456 都匹配了
    print(result.group(1))

    # 贪婪模式下 .*? 则是尽可能少的匹配字符
    # 字符串中间应尽量使用非贪婪匹配，以免出现匹配结果缺失的情况
    result2 = re.match(r'^He.*?(\d+).*Demo$', content)
    # <re.Match object; span=(0, 40), match='Hello 1234567 World_This is a Regex Demo'>
    print(result2)
    # 1234567
    print(result2.group(1))


# 非贪婪匹配
def re_match_non_greed():
    # 需要注意一点，如果匹配的结果在字符串结尾，非贪婪匹配可能匹配不到内容，因为非贪婪是尽可能少的匹配
    content = 'https://weibo.com/comment/KEraCN'
    result1 = re.match(r'https.*?comment/(.*?)', content)
    result2 = re.match(r'https.*?comment/(.*)', content)
    # 结果1：
    print('结果1：', result1.group(1))
    # 结果2： KEraCN
    print('结果2：', result2.group(1))


# 修饰符，常见的还有 re.I，re.L，re.M，re.S，re.U，re.X
def re_match_ornament():
    content = '''Hello 1234567 World_This 
    is a Regex Demo'''
    # re.S 使 . 匹配包括换行符在内的所有字符
    result = re.match(r'^He.*?(\d+).*?Demo$', content, re.S)
    # 因为 HTML 中经常会有换行，所以 re.S 在网页匹配中很常见
    # 1234567
    print(result.group(1))


# 转义匹配，主要应对目标字符串里包含特殊字符的情况
def re_match_transfer():
    content = '(百度)www.baidu.com'
    result = re.match(r'\(百度\)www\.baidu\.com', content)
    # <re.Match object; span=(0, 17), match='(百度)www.baidu.com'>
    print(result)


re_match_target()
re_match_universal()
re_match_greed()
re_match_non_greed()
re_match_ornament()
re_match_transfer()
