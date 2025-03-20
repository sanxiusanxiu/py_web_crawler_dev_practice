from bs4 import BeautifulSoup

html = '''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
'''
# 使用 CSS 选择器，只需要调用 select 方法，传入相应的 CSS 选择器即可
soup = BeautifulSoup(html, 'lxml')
print(soup.select('.panel .panel-heading'))
# 选择所有 ul 节点下面的所有 li 节点
print(soup.select('ul li'))
print(soup.select('#list-2 .element'))
# 打印输出列表中元素的类型，可以看到类型依然是 Tag 类型
print(type(soup.select('ul')[0]))

# select 方法同样支持嵌套选择
# 先选择所有 ul 节点，再遍历每个 ul 节点选择其 li 节点
for ul in soup.select('ul'):
    print(ul.select('li'))

# 获取属性，获取每个 ul 节点的 id 属性
for ul in soup.select('ul'):
    print(ul['id'])
    print(ul.attrs['id'])

# 获取文本，可以用 string 属性，还可以用 get_text
for li in soup.select('li'):
    print('Get Text:', li.get_text())
    print('String:', li.string)
