from parsel import Selector

html = """
<div>
    <ul>
        <li class="item-0">first item</li>
        <li class="item-1"><a href="link2.html">second item</a></li>
        <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
        <li class="item-1 active"><a href="link4.html">fourth item</a></li>
        <li class="item-0"><a href="link5.html">fifth item</a></li>
    </ul>
</div>
"""

selector = Selector(text=html)
# 结果是一个SelectorList对象
items = selector.css('.item-0')
# 这里的item是Selector对象，这样就可以调用其他CSS或者XPath方法
for item in items:
    # get方法从SelectorList里提取第一个Selector对象
    text = item.xpath('.//text()').get()
    print(text)
print('----- get -----↓')
# 注意get只能提取第一个Selector对象
result = selector.xpath('//li[contains(@class, "item-0")]//text()').get()
print(result)
print('----- get all -----↓')
# 如果想提取所有的内容需要使用getall
results = selector.xpath('//li[contains(@class, "item-0")]//text()').getall()
print(results)
print('----- css -----↓')
# 使用CSS方法获取.item-0的文本内容，*表示所有，::text表示文本
results_css = selector.css('.item-0 *::text').getall()
print(results_css)
