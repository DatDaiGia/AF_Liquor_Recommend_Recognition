# -*- coding: utf-8 -*-
import scrapy
from crawl_liquor.items import CrawlLiquorItem
from scrapy_splash import SplashRequest


class SakenowaSpider(scrapy.Spider):
    name = "sakenw"
    allowed_domains = ['sakenowa.com']
    start_urls = ["https://sakenowa.com/en/ranking"]
    
    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, endpoint='render.html', callback=self.parse)
            
    def parse(self, response):
        item = CrawlLiquorItem()
        
        for data in response.xpath():
            