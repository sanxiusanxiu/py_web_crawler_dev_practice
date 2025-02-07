from lxml import etree

text = '''
<div>
<ul>
<li class="item-0"><a href="link1.html">first item</a></li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-inactive"><a href="link3.html">third item</a></li>
<li class="item-1"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a>
</ul>
</div>
'''
# 调用HTML类进行初始化，注意最后一个li节点是缺失的，etree模块可以自动修正html文本
html = etree.HTML(text)
# 输出bytes类型的、修正后的HTML代码
result = etree.tostring(html)
# 转换成str类型
print(result.decode('utf-8'))
