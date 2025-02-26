import requests
from scrapy import signals

NOTIFICATION_URL = 'http://localhost:5000/notify'

class NotificationExtension(object):
    # 实现3个方法，spider_opened、spider_closed和item_scraped，分别对应爬取开始、爬取结束和爬取到Item的处理
    def spider_opened(self, spider):
        # 调用requests向HTTP服务器发送对应的事件
        requests.post(NOTIFICATION_URL, json={
            'event': 'SPIDER_OPENED',  # 事件的名称
            'data': {'spider_name': spider.name},  # 一些附加数据
        })

    def spider_closed(self, spider):
        requests.post(NOTIFICATION_URL, json={
            'event': 'SPIDER_CLOSED',
            'data': {'spider_name': spider.name},
        })

    def item_scraped(self, item, spider):
        requests.post(NOTIFICATION_URL, json={
            'event': 'ITEM_SCRAPED',
            'data': {'spider_name': spider.name, 'item': dict(item)},
        })

    # 将上述方法和对应的Scrapy信号进行关联
    @classmethod
    def from_crawler(cls, crawler):
        ext = cls()
        # Crawler对象里有一个子对象叫作signals，
        crawler.signals.connect(ext.spider_opened, signal=signals.spider_opened)
        # 通过调用signals对象的connect方法，我们可以将Scrapy运行过程中的某个信号和我们自定义的处理方法关联起来
        crawler.signals.connect(ext.spider_closed, signal=signals.spider_closed)
        # 这样在某个事件发生的时候，被关联的处理方法就会被调用
        crawler.signals.connect(ext.item_scraped, signal=signals.item_scraped)
        return ext