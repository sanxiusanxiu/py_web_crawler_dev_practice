from lxml import etree

# 我们在选择的时候某些属性可能同时匹配了多个节点，但是只想要其中的某个节点，如第二个节点或者最后一个节点
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
# 这时可以利用中括号传入索引的方法获取特定次序的节点
html = etree.HTML(text)
# 选取第一个 li 节点，中括号中传入数字 1 即可，注意这里和代码中不同，序号是以 1 开头的，不是以 0 开头
result = html.xpath('//li[1]/a/text()')
print(result)

# 选取最后一个 li 节点，中括号中调用 last 方法即可，返回的便是最后一个 li 节点
result2 = html.xpath('//li[last()]/a/text()')
print(result2)

# 选取位置小于 3 的 li 节点，也就是位置序号为 1 和 2 的节点，得到的结果就是前两个 li 节点
result3 = html.xpath('//li[position()<3]/a/text()')
print(result3)

# 选取倒数第三个 li 节点，中括号中调用 last 方法再减去 2 即可，因为 last 方法代表最后一个，在此基础减 2 就是倒数第三个
result4 = html.xpath('//li[last()-2]/a/text()')
print(result4)
