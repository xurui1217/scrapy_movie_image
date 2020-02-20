# -*- coding: utf-8 -*-
import scrapy
import pandas as pd
from ImageSpider.items import ImagespiderItem


class JobPositionSpider(scrapy.Spider):
    name = 'job_position'
    allowed_domains = ['ygdy8.net']
    start_urls = ['https://www.ygdy8.net/html/gndy/dyzz/20190713/58833.html']#这句话可写可不写 , 没有影响
    def start_requests(self):#重写这个方法
        url = pd.read_csv("movie.csv",usecols=["url"])#读取csv文件,改为你的路径
        # url = url.head(5)#只取前5条数据
        urls=[x  for x in url["url"]]
        for url in urls:
            url='https://www.ygdy8.net/'+url
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        item = ImagespiderItem()
        item['image_urls'] = response.xpath ('//p/img[1]/@src').extract()
        yield item
