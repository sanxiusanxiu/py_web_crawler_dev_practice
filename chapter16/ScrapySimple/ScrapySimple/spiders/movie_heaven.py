import scrapy
from ..items import MovieHeavenItem

class MovieHeavenSpider(scrapy.Spider):
    name = 'movie_heaven'
    allowed_domains = ['www.dytt8.net']
    start_urls = ['https://www.dytt8.net/html/gndy/china/index.html']

    def parse(self, response):
        content_list = response.xpath('//div[@class="co_content8"]//td[2]//a[2]')
        for i in content_list:
            # 获取外页的标题内容和这个标题的路径
            title = i.xpath('./text()').extract_first()
            href = i.xpath('./@href').extract_first()
            # 内页的地址
            inner_url = 'https://www.dytt8.net' + href
            # 对内页进行访问
            yield scrapy.Request(url=inner_url, callback=self.parse_inner, meta={'title': title})
    def parse_inner(self, response):
        src = response.xpath('//div[@id="Zoom"]//img/@src').extract_first()
        # 获取到图片的网址，但这时遇到一个问题，标题和网址不一一对应，可以用Request的meta参数把title传到本函数下
        title = response.meta['title']
        #
        movie = MovieHeavenItem(title=title, src=src)
        yield movie