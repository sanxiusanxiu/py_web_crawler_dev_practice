from lxml import etree

# XPath 提供了很多节点轴选择方法，包括获取子元素、兄弟元素、父元素、祖先元素等
text = '''
<div>
    <ul>
         <li class="item-0"><a href="link1.html"><span>first item</span></a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a>
     </ul>
 </div>
'''
html = etree.HTML(text)
# 调用 ancestor 轴可以获取所有祖先节点，其后需要跟两个冒号，然后是节点的选择器，这里我们直接使用 *，表示匹配所有节点
result = html.xpath('//li[1]/ancestor::*')
print(result)

# 在冒号后面加了 div，这样得到的结果就只有 div 这个祖先节点
result2 = html.xpath('//li[1]/ancestor::div')
print(result2)

# 调用 attribute 轴可以获取所有属性值，其后跟的选择器还是 *，这代表获取节点的所有属性
result3 = html.xpath('//li[1]/attribute::*')
print(result3)

# 调用 child 轴可以获取所有直接子节点，这里加限定条件，选取 href 属性为 link1.html 的 a 节点
result4 = html.xpath('//li[1]/child::a[@href="link1.html"]')
print(result4)

# 调用 descendant 轴可以获取所有子孙节点，这里加限定条件获取 span 节点
result5 = html.xpath('//li[1]/descendant::span')
print(result5)

# 调用 following 轴可以获取当前节点之后的所有节点，这里获取第二个后续节点
result6 = html.xpath('//li[1]/following::*[2]')
print(result6)

# 调用 following-sibling 轴可以获取当前节点之后的所有同级节点
result7 = html.xpath('//li[1]/following-sibling::*')
print(result7)
