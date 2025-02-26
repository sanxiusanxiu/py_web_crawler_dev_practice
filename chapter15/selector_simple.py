from scrapy import Selector

body = '<html><head><title>Hello World</title></head><body></body></html>'
# 构建selector对象
selector = Selector(text=body)
title = selector.xpath('//title/text()').extract_first()
print(title)  # Hello World
