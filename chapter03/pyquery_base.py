from pyquery import PyQuery as pq

# 基本 CSS 选择器
def pyquery_css_selector():
    html = '''
    <div id="container">
        <ul class="list">
             <li class="item-0">first item</li>
             <li class="item-1"><a href="link2.html">second item</a></li>
             <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
             <li class="item-1 active"><a href="link4.html">fourth item</a></li>
             <li class="item-0"><a href="link5.html">fifth item</a></li>
         </ul>
     </div>
    '''
    # 初始化 PyQuery 对象之后，传入一个 CSS 选择器 #container .list li
    doc = pq(html)
    # 先选取 id 为 container 的节点，然后再选取其内部的 class 为 list 的节点内部的所有 li 节点
    print(doc('#container .list li'))
    print(type(doc('#container .list li')))

    # 查找子节点需要用到 find 方法，传入的参数是 CSS 选择器
    # 选取 class 为 list 的节点，然后调用了 find() 方法，传入 CSS 选择器，选取其内部的 li 节点
    items = doc('.list')
    print(type(items))
    print(items)
    lis = items.find('li')
    # find() 方法会将符合条件的所有节点选择出来，结果的类型是 PyQuery 类型
    print(type(lis))
    print(lis)
    # find 的查找范围是节点的所有子孙节点，如果只想查找子节点，那可以用 children 方法
    lis = items.children()
    print(type(lis))
    print(lis)
    # 如果要筛选所有子节点中符合条件的节点
    # 比如想筛选出子节点中 class 为 active 的节点，可以向 children() 方法传入 CSS 选择器.active
    lis = items.children('.active')
    print(lis)

# 查找节点
def pyquery_find_node():
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
    # 我们可以用 parent 方法来获取某个节点的父节点
    doc = pq(html)
    # 首先用.list 选取 class 为 list 的节点
    items = doc('.list')
    # 然后调用 parent 方法得到其父节点
    container = items.parent()
    # 其类型依然是 PyQuery 类型
    print(type(container))
    # 这里的父节点是该节点的直接父节点，也就是说，它不会再去查找父节点的父节点，即祖先节点
    print(container)
    # 但是如果想获取某个祖先节点，该怎么办呢？这时可以用 parents 方法
    parents = items.parents()
    print(type(parents))
    print(parents)
    # 如果想要筛选某个祖先节点的话，可以向 parents 方法传入 CSS 选择器，这样就会返回祖先节点中符合 CSS 选择器的节点
    parent = items.parents('.wrap')
    print(parent)

    # 兄弟节点
    # 如果要获取兄弟节点，可以使用 siblings() 方法
    li = doc('.list .item-0.active')
    # 首先选择 class 为 list 的节点内部 class 为 item-0 和 active 的节点，也就是第三个 li 节点
    # 它的兄弟节点有 4 个，那就是第一、二、四、五个 li 节点
    print(li.siblings())
    # 如果要筛选某个兄弟节点，我们依然可以向 siblings 方法传入 CSS 选择器，这样就会从所有兄弟节点中挑选出符合条件的节点
    print(li.siblings('.active'))

# pyquery_css_selector()
# pyquery_find_node()
