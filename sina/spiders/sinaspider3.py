# -*- coding: utf-8 -*-

import scrapy
import json
import re
from items import  getnum3,getlocation_gender_name,Sina_Item3,processcook

class Sinaspider3Spider(scrapy.Spider):
    custom_settings = {
        'ITEM_PIPELINES': {'sina.pipelines.SinaPipeline3': 400, },
    }
    name = 'sinaspider3'
    # allowed_domains = ['www.weibo.com']
    start_urls = ['https://m.weibo.cn/api/container/getIndex?containerid=231051_-_fans_-_3261134763&since_id=17']
    # baseapi='https://m.weibo.cn/api/container/getIndex?containerid=231051_-_fans_-_3261134763&since_id='
    baseurl='https://weibo.cn/u/'
    index=1
    cnt=0
    def parse(self, response):
      dic=json.loads(response.text)
      uid = []
      if  'cards' in dic["data"].keys():
        users=dic["data"]['cards'][0]['card_group']
        for each in users:
          if 'user' in each.keys():
            uid.append(each['user']['id'])
        for each in uid:
            yield scrapy.Request(self.baseurl+str(each),cookies=self.cook,callback=self.parse_detail)
        self.index+=1
        url=self.baseapi+str(self.index)
        yield scrapy.Request(url, cookies=self.cook,callback=self.parse)
      else:
        pass

    def parse_detail(self,response):
        location_and_username=response.xpath("//div[@class='u']/table//span[@class='ctt']")
        location_and_username=location_and_username.xpath("string(.)").extract()[0]
        webnum=response.xpath("//div[@class='u']/div[@class='tip2']/span/text()").extract()[0]
        fans=response.xpath("//div[@class='u']/div[@class='tip2']/a[2]/text()").extract()[0]
        follow=response.xpath("//div[@class='u']/div[@class='tip2']/a[1]/text()").extract()[0]
        sina_item3 =Sina_Item3()
        sina_item3['webnum']=getnum3(webnum)
        sina_item3['follow']=getnum3(follow)
        sina_item3['fans']=getnum3(fans)
        sina_item3['location'],sina_item3['gender'],sina_item3['username']=getlocation_gender_name(location_and_username)
        sina_item3["cookie"]=self.settings.get("COOKIE")
        yield sina_item3

    def start_requests(self):
        # yield scrapy.Request("https://weibo.cn/u/2290732425",cookies=self.cook)
        self.cook = processcook(self.settings.get("COOKIE"))
        self.baseapi="https://m.weibo.cn/api/container/getIndex?containerid=231051_-_fans_-_"+self.settings.get("URL")+"&type=all"+"&since_id="
        url = self.baseapi + str(self.index)
        yield scrapy.Request(url, cookies=self.cook,callback=self.parse)
