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

result_css = selector.css('.item-0.active a::attr(href)').get()
print(result_css)

result_xpath = selector.xpath('//li[contains(@class, "item-0") and contains(@class, "active")]/a/@href').get()
print(result_xpath)
