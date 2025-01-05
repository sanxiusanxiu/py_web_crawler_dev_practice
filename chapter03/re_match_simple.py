import re

content = 'Hello 123 4567 World_This is a Regex Demo.'
print(len(content))
result = re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}', content)
print(result)
# 输出匹配到的内容
print(result.group())
# 输出匹配的范围
print(result.span())
