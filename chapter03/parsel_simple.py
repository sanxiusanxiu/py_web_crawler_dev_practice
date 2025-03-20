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
# 创建一个 Selector 对象
selector = Selector(text=html)

# 分别使用 CSS 和 XPath 提取 class 包含 .item-0 的节点
items_css = selector.css('.item-0')
print(len(items_css), type(items_css), items_css)
print('----- -----')

item_xpath = selector.xpath('//li[contains(@class, "item-0")]')
print(len(item_xpath), type(item_xpath), item_xpath)
