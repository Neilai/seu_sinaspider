# -*- coding: utf-8 -*-
import scrapy
import time
from selenium import webdriver
from scrapy.selector import Selector
from items import SinaItem2,getnum,stripspace,deletespace,matchnum,processcook,processdatetime
import json
import re

class Sinaspider2Spider(scrapy.Spider):
    name = 'sinaspider2'
    custom_settings = {
        'ITEM_PIPELINES': {'sina.pipelines.SinaPipeline2': 300, },
    }
    allowed_domains = ['www.weibo.com']
    start_urls = ["http://weibo.com/3261134763/Ffztb4w7W?from=page_1006053261134763_profile&wvr=6&mod=weibotime&type=comment#_rnd1501944199917"]
    flag=0
    page=0
    cnt=0
    baseurl="http://weibo.com/aj/v6/mblog/info/big?ajwvr=6"

    def __init__(self, cookie, url, **kwargs):
        print(cookie)
        self.starturl = url
        self.oldcook = cookie
        self.cook = processcook(cookie)

    def parse(self, response):
        result=json.loads(response.text)['data']['html']
        datetime=Selector(text=result).xpath("//div[contains(@class,'list_li') and contains(@class,'S_line1') and contains(@class,'clearfix')]/div[@class='list_con']//div[contains(@class,'WB_from') and contains(@class,'S_txt2')]/a[1]/text()").extract()
        repeatname = Selector(text=result).xpath("//div[contains(@class,'list_li') and contains(@class,'S_line1') and contains(@class,'clearfix')]/div[@class='list_con']/div[@class='WB_text']/a[1]/text()").extract()
        repeatnum=Selector(text=result).xpath("//div[contains(@class,'list_li') and contains(@class,'S_line1') and contains(@class,'clearfix')]/div[@class='list_con']/div[contains(@class,'WB_func') and contains(@class,'clearfix')]/div/ul/li[2]/span/a[1]/text()").extract()
        matchnum(repeatnum)
        sina_item2 = SinaItem2()
        sina_item2['repeatnum']=repeatnum
        sina_item2['datetime']=datetime
        sina_item2['repeatname']=repeatname
        sina_item2['cookie'] = self.oldcook
        yield sina_item2

    def start_requests(self):
        # yield scrapy.Request("http://weibo.com/aj/v6/mblog/info/big?ajwvr=6&id=4121910092307199&__rnd=1501772409505", cookies=self.cook)
        yield scrapy.Request(self.starturl,cookies=self.cook,callback=self.getmid)

    def getmid(self,response):
        result=re.search(r'mid=(\d+)',response.text,re.DOTALL)
        #mid='4137112691076812'
        url=self.baseurl+'&'+'id='+result.group(1)+'&'+'page=1'
        yield scrapy.Request(url,cookies=self.cook,dont_filter=True,callback=self.generate_page,meta={'mid':result.group(1)})

    def generate_page(self,response):
        dic=json.loads(response.text)
        if 'page' in dic['data'].keys():
            self.page = dic['data']['page']['totalpage']
        else:
            self.page=1
        mid = response.meta.get('mid', '')
        print(self.page)
        iterator =1
        while iterator <= self.page:
            url = self.baseurl+'&'+'id='+mid+'&' + 'page='+str(iterator)
            yield scrapy.Request(url, cookies=self.cook, dont_filter=True, callback=self.parse)
            iterator = iterator + 1
