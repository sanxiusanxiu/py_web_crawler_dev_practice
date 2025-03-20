from bs4 import BeautifulSoup

# 根据节点名来查询元素
def bs4_node_name_selector(html):
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
    soup = BeautifulSoup(html, 'lxml')
    # find_all 查询所有符合条件的元素，find_all(name , attrs , recursive , text , **kwargs)
    # 根据节点名来查询元素
    print(soup.find_all(name='ul'))
    print(type(soup.find_all(name='ul')[0]))
    # 因为都是 Tag 类型，所以依然可以进行嵌套查询，再继续查询其内部的 li 节点
    for ul in soup.find_all(name='ul'):
        print(ul.find_all(name='li'))
        # 遍历每个 li 获取它的文本
        for li in ul.find_all(name='li'):
            print(li.string)

# 根据属性进行查询
def bs4_attr_name_selector():
    html = '''
    <div class="panel">
        <div class="panel-heading">
            <h4>Hello</h4>
        </div>
        <div class="panel-body">
            <ul class="list" id="list-1" name="elements">
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
    soup = BeautifulSoup(html, 'lxml')
    print(soup.find_all(attrs={'id': 'list-1'}))
    print(soup.find_all(attrs={'name': 'elements'}))
    # 对于一些常用的属性，比如 id 和 class 等，我们可以不用 attrs 来传递
    # 比如，要查询 id 为 list-1 的节点，可以直接传入 id 这个参数
    print(soup.find_all(id='list-1'))
    # 由于 class 在 Python 里是一个关键字，所以后面需要加一个下划线
    print(soup.find_all(class_='element'))

# 根据文本进行匹配
def bs4_text_selector():
    import re
    html = '''
    <div class="panel">
        <div class="panel-body">
            <a>Hello, this is a link</a>
            <a>Hello, this is a link, too</a>
        </div>
    </div>
    '''
    soup = BeautifulSoup(html, 'lxml')
    # text参数可用来匹配节点的文本，传入的形式可以是字符串，也可以正则表达式对象
    print(soup.find_all(text=re.compile('link')))

# 匹配首个（单个）元素
def bs4_find_selector():
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
    soup = BeautifulSoup(html, 'lxml')
    # find 方法返回的是单个元素，也就是第一个匹配的元素，find_all 返回的是所有匹配的元素组成的列表
    print(soup.find(name='ul'))
    # 返回结果不再是列表形式，而是第一个匹配的节点元素，类型依然是 Tag 类型
    print(type(soup.find(name='ul')))
    print(soup.find(class_='list'))

"""
另外还有许多的查询方法，用法与前面介绍的 find_all、find 方法完全相同，只不过查询范围不同
find_parents 和 find_parent：前者返回所有祖先节点，后者返回直接父节点
find_next_siblings 和 find_next_sibling：前者返回后面所有的兄弟节点，后者返回后面第一个兄弟节点
find_previous_siblings 和 find_previous_sibling：前者返回前面所有的兄弟节点，后者返回前面第一个兄弟节点
find_all_next 和 find_next：前者返回节点后所有符合条件的节点，后者返回第一个符合条件的节点
find_all_previous 和 find_previous：前者返回节点前所有符合条件的节点，后者返回第一个符合条件的节点

"""

# bs4_node_name_selector()
# bs4_attr_name_selector()
# bs4_text_selector()
# bs4_find_selector()
