from lxml import etree

# 直接读取文件进行解析
html = etree.parse('./xpath_test.html', etree.HTMLParser())
result = etree.tostring(html)
# 输出结果会多一个 DOCTYPE 声明，不过对解析无任何影响
print(result.decode('utf-8'))

# 一般会用 // 开头的 XPath 规则来选取所有符合要求的节点
# 这里使用 * 代表匹配所有节点，也就是整个 HTML 文本中的所有节点都会被获取
result2 = html.xpath('//*')
# print(result2)

# 获取所有 li 节点
result3 = html.xpath('//li')
# print(result3)
# print(result3[0])

# 通过 / 或 // 即可查找元素的子节点或子孙节点
# 选择 li 节点的所有直接 a 子节点
result4 = html.xpath('//li/a')
# print(result4)

# 获取 ul 节点下的所有子孙 a 节点，注意 / 用于获取直接子节点，// 用于获取子孙节点
result5 = html.xpath('//ul//a')
# print(result5)

# 如果这里用 //ul/a 就无法获取任何结果了
# 因为 / 用于获取直接子节点，而在 ul 节点下没有直接的 a 子节点，只有 li 节点
result6 = html.xpath('//ul/a')
# print(result6)

# 首先选中 href 属性为 link4.html 的 a 节点，然后再获取其父节点，然后再获取其 class 属性
result7 = html.xpath('//a[@href="link4.html"]/../@class')
# print(result7)

# 也可以通过 parent:: 来获取父节点
result8 = html.xpath('//a[@href="link4.html"]/parent::*/@class')
# print(result8)

# 可以用 @ 符号进行属性过滤
# 选取 class 为 item-0 的 li 节点
result9 = html.xpath('//li[@class="item-0"]')
# print(result9)

# 使用 text 方法获取节点中的文本
# 获取前面 li 节点中的文本，有两种方式，一种是先选取 a 节点再获取文本，另一种就是使用 //
result10 = html.xpath('//li[@class="item-0"]/a/text()')
# print(result10)  # 更整洁

result11 = html.xpath('//li[@class="item-0"]//text()')
# print(result11)  # 更全面

# 获取所有 li 节点下所有 a 节点的 href 属性值
result12 = html.xpath('//li/a/@href')
# print(result12)

# 有时候某些节点的某个属性可能有多个值
text2 = '''  
<li class="li li-first"><a href="link.html">first item</a></li> 
'''
html2 = etree.HTML(text2)
# 获取 li 节点 class 属性为 li 的值，如果还使用之前的属性匹配获取，就无法匹配了
result13 = html2.xpath('//li[@class="li"]/a/text()')
# print(result13)
# 这时需要用到 contains 方法，第一个参数传入属性名称，第二个参数传入属性值，只要此属性包含所传入的属性值，就可以完成匹配
result14 = html2.xpath('//li[contains(@class, "li")]/a/text()')
# print(result14)

# 另外，我们可能还遇到一种情况，那就是根据多个属性确定一个节点，这时就需要同时匹配多个属性
text3 = '''
<li class="li li-first" name="item"><a href="link.html">first item</a></li>
'''
html3 = etree.HTML(text3)
# 此时可以使用运算符 and 来连接，由此可见 XPath 也可以使用运算符
result15 = html3.xpath('//li[contains(@class, "li") and @name="item"]/a/text()')
# print(result15)
