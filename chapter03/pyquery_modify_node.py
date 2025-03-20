from pyquery import PyQuery as pq

# addClass 和 removeClass
def pyquery_add_remove_class():
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
    # 首先选中第三个 li 节点
    li = doc('.item-0.active')
    print(li)
    # 然后调用 removeClass() 方法，将 li 节点的 active 这个 class 移除
    li.removeClass('active')
    print(li)
    # 后来又调用 addClass() 方法，将 class 添加回来
    li.addClass('active')
    print(li)

# attr、text、html
def pyquery_attr_text_html():
    html = '''
    <ul class="list">
         <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
    </ul>
    '''
    doc = pq(html)
    # 首先选中 li 节点
    li = doc('.item-0.active')
    print(li)
    # 然后调用 attr 方法来修改属性，该方法的第一个参数为属性名，第二个参数为属性值
    li.attr('name', 'link')
    print(li)
    # 调用 text 和 html 方法来改变节点内部的内容
    li.text('changed item')
    print(li)
    li.html('<span>changed item</span>')
    print(li)

# remove
def pyquery_remove():
    html = '''
    <div class="wrap">
        Hello, World
        <p>This is a paragraph.</p>
     </div>
    '''
    # 现在想提取 Hello, World 这个字符串，而不要 p 节点内部的字符串
    doc = pq(html)
    wrap = doc('.wrap')
    print(wrap.text())
    # 首先选中 p 节点，然后调用 remove() 将其移除，这时 wrap 内部就只剩下 Hello, World ，然后再利用 text() 方法提取
    wrap.find('p').remove()
    print(wrap.text())

# pyquery_add_remove_class()
# pyquery_attr_text_html()
# pyquery_remove()
