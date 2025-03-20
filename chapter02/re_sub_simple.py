import re

content = '54aK54yea54TUbs2g'
content = re.sub(r'\d+', '', content)
# aKyeaTUbsg
print(content)
