import scrapy

from tutorial.items import Douban

class DmozSpider(scrapy.spiders.Spider):#第一步
    #一定要定义的三个属性
    name = "dmoz"
    allowed_domains =["dmoztools.net"]#镜像网页，原网页不可用·规范爬虫爬取的范围
    start_urls = [
        "http://www.dmoztools.net/Computers/Programming/Languages/Python/Books/",
        "http://www.dmoztools.net/Computers/Programming/Languages/Python/Resources/"

    ]

    def parse(self,response):#第二步
        for sel in response.xpath('//ul/li'):
            title = sel.xpath('a/text()').extract()
            link = sel.xpath('a/@href').extract()
            desc = sel.xpath('text()').extract()
            print (title, link, desc)