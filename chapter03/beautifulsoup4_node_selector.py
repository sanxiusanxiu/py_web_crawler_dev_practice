from bs4 import BeautifulSoup

# 选择元素提取信息
def bs4_get_attribute():
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
    soup = BeautifulSoup(html, 'lxml')
    # 直接调用节点的名称就可以选择节点元素，再调用 string 属性就可以得到节点内的文本，这种选择方式速度非常快
    print(soup.title)
    print(type(soup.title))
    print(soup.title.string)
    # 如果单个节点结构层次非常清晰，可以选用这种方式来解析
    print(soup.head)
    print(soup.p)
    # 利用 name 属性获取节点的名称
    print(soup.title.name)
    # 每个节点可能有多个属性，可以调用 attrs 获取所有属性
    print(soup.p.attrs)
    print(soup.p.attrs['name'])
    # 获取 name 属性
    print(soup.p['name'])
    print(soup.p['class'])
    # 利用 string 属性获取节点元素包含的文本内容
    print(soup.p.string)

# 嵌套选择
def bs4_get_double():
    html = """
    <html><head><title>The Dormouse's story</title></head>
    <body>
    """
    soup = BeautifulSoup(html, 'lxml')
    # 调用 head 之后再次调用 title
    print(soup.head.title)
    print(type(soup.head.title))
    print(soup.head.title.string)

# 关联选择
def bs4_correlation_node():
    html = """
    <html>
        <head>
            <title>The Dormouse's story</title>
        </head>
        <body>
            <p class="story">
                Once upon a time there were three little sisters; and their names were
                <a href="https://example.com/elsie" class="sister" id="link1">
                    <span>Elsie</span>
                </a>
                <a href="https://example.com/lacie" class="sister" id="link2">Lacie</a> 
                and
                <a href="https://example.com/tillie" class="sister" id="link3">Tillie</a>
                and they lived at the bottom of a well.
            </p>
            <p class="story">...</p>
    """
    # 在做选择的时候，有时候不能做到一步就选到想要的节点元素，需要先选中某一个节点元素，然后以它为基准再选择它的子节点、父节点、兄弟节点等
    soup = BeautifulSoup(html, 'lxml')
    # contents 属性得到的结果是直接子节点的列表
    print(soup.p.contents)
    # 调用 children 属性也可以得到相应的结果，不过返回值是生成器类型
    print(soup.p.children)
    for i, child in enumerate(soup.p.children):
        print(i, child)
    # 如果要得到所有的子孙节点的话，可以调用 descendants 属性，descendants 会递归查询所有子节点，得到所有的子孙节点
    print(soup.p.descendants)
    for i, child in enumerate(soup.p.descendants):
        print(i, child)

# 关联选择2
def bs4_correlation_node2():
    # 如果要获取某个节点元素的父节点，可以调用 parent 属性
    html = """
    <html>
        <head>
            <title>The Dormouse's story</title>
        </head>
        <body>
            <p class="story">
                Once upon a time there were three little sisters; and their names were
                <a href="https://example.com/elsie" class="sister" id="link1">
                    <span>Elsie</span>
                </a>
            </p>
            <p class="story">...</p>
    """
    soup = BeautifulSoup(html, 'lxml')
    # 需要注意的是，这里输出的仅仅是 a 节点的直接父节点，而没有再向外寻找父节点的祖先节点
    print(soup.a.parent)
    # 如果想获取所有的祖先节点，可以调用 parents 属性
    print(type(soup.a.parents))
    print(list(enumerate(soup.a.parents)))


# 获取同级的节点（也就是兄弟节点）
def bs4_correlation_node3():
    html = """
    <html>
        <body>
            <p class="story">
                Once upon a time there were three little sisters; and their names were
                <a href="https://example.com/elsie" class="sister" id="link1">
                    <span>Elsie</span>
                </a>
                Hello
                <a href="https://example.com/lacie" class="sister" id="link2">Lacie</a> 
                and
                <a href="https://example.com/tillie" class="sister" id="link3">Tillie</a>
                and they lived at the bottom of a well.
            </p>
    """
    soup = BeautifulSoup(html, 'lxml')
    # next_sibling 和 previous_sibling 分别获取节点的下一个和上一个兄弟元素
    # next_siblings 和 previous_siblings 则分别返回后面和前面的兄弟节点
    print('Next Sibling', soup.a.next_sibling)
    print('Prev Sibling', soup.a.previous_sibling)
    print('Next Siblings', list(enumerate(soup.a.next_siblings)))
    print('Prev Siblings', list(enumerate(soup.a.previous_siblings)))
    # 提取信息
    # 如果返回结果是单个节点，那么可以直接调用 string、attrs 等属性获得其文本和属性
    # 如果返回结果是多个节点的生成器，则可以转为列表后取出某个元素，然后再调用 string、attrs 等属性获取其对应节点的文本和属性
    print('Next Sibling:')
    print(type(soup.a.next_sibling))
    print(soup.a.next_sibling)
    print(soup.a.next_sibling.string)
    print('Parent:')
    print(type(soup.a.parents))
    print(list(soup.a.parents)[0])
    print(list(soup.a.parents)[0].attrs['class'])
