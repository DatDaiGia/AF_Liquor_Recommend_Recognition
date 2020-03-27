# -*- coding: utf-8 -*-
import scrapy


class CrawlLiquorItem(scrapy.Item):
    name = scrapy.Field()
    intl_name = scrapy.Field()
    year_month = scrapy.Field()
    rank = scrapy.Field()
    score = scrapy.Field()
    f1 = scrapy.Field()
    f2 = scrapy.Field()
    f3 = scrapy.Field()
    f4 = scrapy.Field()
    f5 = scrapy.Field()
    f6 = scrapy.Field()
    flavour_tags = scrapy.Field()
