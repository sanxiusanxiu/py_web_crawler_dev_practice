from bs4 import BeautifulSoup


def bs4_demo_pre():
    # bs4一般都是使用 lxml 解析器，也可以使用 html.parser 、xml 、html5lib 等
    soup = BeautifulSoup('<p>Hello</p>', 'lxml')
    print(soup.p.string)

bs4_demo_pre()

print('-- - --')

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="https://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="https://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="https://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

# 不标准的 HTML 字符串在初始化 BeautifulSoup 时会自动修正
soup = BeautifulSoup(html, 'lxml')
# prettify方法可以把要解析的字符串以标准的缩进格式输出
print(soup.prettify())
# soup.title.string是输出 HTML 中 title 节点的文本内容
print(soup.title.string)
