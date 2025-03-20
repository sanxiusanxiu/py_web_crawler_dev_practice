import re

content1 = '2019-12-15 12:00'
content2 = '2019-12-17 12:55'
content3 = '2019-12-22 13:21'

pattern = re.compile(r'\d{2}:\d{2}')

result1 = re.sub(pattern, '', content1)
result2 = re.sub(pattern, '', content2)
result3 = re.sub(pattern, '', content3)
# 2019-12-15  2019-12-17  2019-12-22
print(result1, result2, result3)
