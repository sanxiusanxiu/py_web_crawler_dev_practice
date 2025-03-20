from urllib.parse import urljoin

# 如果基础链接里提供了 scheme、netloc、path，新的链接里不存在 scheme、netloc、path就会进行补充，如果新链接里有 scheme、netloc、path 则使用新链接的内容

# http://www.baidu.com/FAQ.html
print(urljoin('http://www.baidu.com', 'FAQ.html'))

# https://cuiqingcai.com/FAQ.html
print(urljoin('http://www.baidu.com', 'https://cuiqingcai.com/FAQ.html'))

# https://cuiqingcai.com/FAQ.html
print(urljoin('http://www.baidu.com/about.html', 'https://cuiqingcai.com/FAQ.html'))

# https://cuiqingcai.com/FAQ.html?question=2
print(urljoin('http://www.baidu.com/about.html', 'https://cuiqingcai.com/FAQ.html?question=2'))

# https://cuiqingcai.com/index.php
print(urljoin('http://www.baidu.com?wd=abc', 'https://cuiqingcai.com/index.php'))

# http://www.baidu.com?category=2#comment
print(urljoin('http://www.baidu.com', '?category=2#comment'))

# www.baidu.com?category=2#comment
print(urljoin('www.baidu.com', '?category=2#comment'))

# www.baidu.com?category=2
print(urljoin('www.baidu.com#comment', '?category=2'))
