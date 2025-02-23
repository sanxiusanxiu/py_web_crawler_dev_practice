import scrapy
from ..items import QuoteItem

# QuotesSpider 就是genspider命令自动创建的spider
class QuotesSpider(scrapy.Spider):
    # spider的名称
    name = "quotes"
    # 允许爬取的域名
    allowed_domains = ["quotes.toscrape.com"]
    # 初始请求
    start_urls = ["https://quotes.toscrape.com"]

    def parse(self, response):
        quotes = response.css('.quote')
        for quote in quotes:
            item = QuoteItem()
            item['text'] = quote.css('.text::text').extract_first()
            item['author'] = quote.css('.author::text').extract_first()
            item['tags'] = quote.css('.tags .tag::text').extract()
            yield item

        next_page = response.css('.pager .next a::attr(href)').extract_first()
        url = response.urljoin(next_page)
        yield scrapy.Request(url, callback=self.parse)
