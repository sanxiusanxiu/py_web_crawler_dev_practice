from lxml import etree

text = """
<div>
<ul>
<li class="item-0"><a href="link1.html">first item</a></li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-inactive"><a href="link3.html">third item</a></li>
<li class="item-1"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a>
</ul>
</div>
"""

# 调用 HTML 类进行初始化，构造一个 XPath 解析对象
html = etree.HTML(text)
# 输出 bytes 类型的 HTML 代码  # 注意最后一个 li 节点是缺失的，etree 模块可以自动修正 html 文本
result = etree.tostring(html)
# print(result)
# 转换成 str 类型
print(result.decode('utf-8'))
