import re

content = 'Hello 123 4567 World_This is a Regex Demo.'
# 42
print(len(content))

result = re.match(r'^Hello\s\d\d\d\s\d{4}\s\w{10}', content)
# <re.Match object; span=(0, 25), match='Hello 123 4567 World_This'>
print(result)
# 输出匹配到的内容 Hello 123 4567 World_This
print(result.group())
# 输出匹配的范围 (0, 25)
print(result.span())
