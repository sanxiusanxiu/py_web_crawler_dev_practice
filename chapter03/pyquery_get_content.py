from pyquery import PyQuery as pq

# 调用 attr() 方法获取属性
def pyquery_get_attr():
    html = '''
    <div class="wrap">
        <div id="container">
            <ul class="list">
                 <li class="item-0">first item</li>
                 <li class="item-1"><a href="link2.html">second item</a></li>
                 <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
                 <li class="item-1 active"><a href="link4.html">fourth item</a></li>
                 <li class="item-0"><a href="link5.html">fifth item</a></li>
             </ul>
         </div>
     </div>
    '''
    doc = pq(html)
    # 首先选中 class 为 item-0 和 active 的 li 节点内的 a 节点，它的类型是 PyQuery 类型
    a = doc('.item-0.active a')
    print(a, type(a))
    # 然后调用 attr 方法，传入属性的名称，得到这个属性的值
    print(a.attr('href'))
    # 也可以通过调用 attr 属性来获取属性
    print(a.attr.href)

    # 当返回结果包含多个节点时，调用 attr 方法，只会得到第一个节点的属性
    a = doc('a')
    print(a, type(a))
    print(a.attr('href'))
    print(a.attr.href)
    # 遇到这种情况时，就要用到前面所说的遍历了
    for item in a.items():
        print(item.attr('href'))

# 调用 text 方法获取文本
def pyquery_get_text():
    html = '''
    <div class="wrap">
        <div id="container">
            <ul class="list">
                 <li class="item-0">first item</li>
                 <li class="item-1"><a href="link2.html">second item</a></li>
                 <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
                 <li class="item-1 active"><a href="link4.html">fourth item</a></li>
                 <li class="item-0"><a href="link5.html">fifth item</a></li>
             </ul>
         </div>
     </div>
    '''
    doc = pq(html)
    # 首先选中一个 a 节点，然后调用 text 方法，就可以获取其内部的文本信息
    a = doc('.item-0.active a')
    print(a)
    print(a.text())
    # 如果想要获取这个节点内部的 HTML 文本，需要使用 html 方法
    li = doc('.item-0.active')
    print(li)
    print(li.html())

    # 如果选中的结果是多个节点
    # html 方法返回的是第一个 li 节点的内部 HTML 文本
    # text 则返回了所有的 li 节点内部的纯文本，中间用一个空格分割开，即返回结果是一个字符串
    li = doc('li')
    print(li.html())
    print(li.text())
    print(type(li.text()))
