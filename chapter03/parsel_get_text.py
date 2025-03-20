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
# 返回的是一个 SelectorList 对象
items = selector.css('.item-0')

# 这里的 item 是 Selector 对象，这样就可以调用其他 CSS 或者 XPath 方法
for item in items:
    # get 方法从 SelectorList 里提取第一个 Selector 对象
    text = item.xpath('.//text()').get()
    print(text)
print('----- get 方法 ↓ -----')
# 注意 get 只能提取第一个 Selector 对象
result = selector.xpath('//li[contains(@class, "item-0")]//text()').get()
print(result)
print('----- get all 方法 ↓ -----')
# 如果想提取所有的内容需要使用 getall
results = selector.xpath('//li[contains(@class, "item-0")]//text()').getall()
print(results)
print('----- css 方法 ↓ -----')
# 使用 CSS 方法获取 .item-0 的文本内容，* 表示所有，::text 表示文本
results_css = selector.css('.item-0 *::text').getall()
print(results_css)
