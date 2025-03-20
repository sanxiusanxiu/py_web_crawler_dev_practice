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
# 匹配包含 link 的所有结果
result = selector.css('.item-0').re('link.*')
print(result)

# 进一步提取
result2 = selector.css('.item-0 *::text').re('.*item')
print(result2)

# 提取第一个符合规则的结果
result_first = selector.css('.item-0').re_first('<span class="bold">(.*?)</span>')
print(result_first)
