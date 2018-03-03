# -*- coding: utf-8 -*-
import scrapy
import re
from items import SinaItem4,processcook
class Sinaspider4Spider(scrapy.Spider):
    name = 'sinaspider4'
    custom_settings = {
        'ITEM_PIPELINES': {'sina.pipelines.SinaPipeline4': 500, },
    }
    allowed_domains = ['www.weibo.cn']
    start_urls = ['https://weibo.cn/2613164393/fans']
    #uid=2613164393

    baseurl="https://weibo.cn/{0}/fans?page={1}"

    def __init__(self,cookie,url,**kwargs):

        self.uid =url
        self.oldcook = cookie
        self.cook = processcook(cookie)

    def parse_url(self, response):

        level=response.meta.get('level')
        uid=response.meta.get('uid')
        name = response.meta.get('name','')
        if not name:
             try:
                 location_and_username = response.xpath("//div[@class='u']/table//span[@class='ctt']")
                 location_and_username = location_and_username.xpath("string(.)").extract()[0]
                 name = re.search(r'(\S+)', location_and_username).group(1)

             except:
                 name="我"

        # page=3
        # if not response.xpath("//div[@class='pa']//div//input[1]/@value").extract():
        #     total=1
        # else:
        #     total=int(response.xpath("//div[@class='pa']//div//input[1]/@value").extract()[0])
        # if total<3:
        #     page=total

        # for cnt in range(page):
        #     url= self.baseurl.format(uid,cnt+1)
        #     yield scrapy.Request(url, cookies=self.cook, callback=self.parse_detail,meta={'level': level,'name':name},dont_filter=True)

        url = self.baseurl.format(uid,1)
        yield scrapy.Request(url, cookies=self.cook, callback=self.parse_detail, meta={'level': level, 'name': name}, dont_filter=True)


    def parse_detail(self, response):
        level = response.meta.get('level')
        parentname = response.meta.get('name')
        fans_id = []
        sina_item4 = SinaItem4()
        level_list=[]
        parentname_list=[]

        fans_urls=response.xpath("//div[@class='c']//table//td[2]/a[1]/@href").extract()
        fans_name = response.xpath("//div[@class='c']//table//td[2]/a[1]/text()").extract()

        for i in range(len(fans_urls)):
            level_list.append(level)
            parentname_list.append(parentname)
        sina_item4['fanslevel']=level_list
        sina_item4['fansparent']=parentname_list
        sina_item4['fansname']=fans_name
        sina_item4['cookie'] = self.oldcook
        yield sina_item4
        for  each in fans_urls:
            fans_id.append(re.search(r"\d+",each).group())
        cnt=0

        if level<3:
            for uid in fans_id:
                url=self.baseurl.format(uid,1)
                if  fans_name[cnt]!="新手指南" :
                    yield scrapy.Request(url,cookies=self.cook, callback=self.parse_url,meta={'level': level+1,'uid':uid,'name':fans_name[cnt]},dont_filter=True)
                cnt+=1

    def start_requests(self):
        # yield scrapy.Request("https://weibo.cn/u/2290732425",cookies=self.cook)
        url="https://weibo.cn/u/"+self.uid
        yield scrapy.Request(url, cookies=self.cook, callback=self.parse_url,meta={'level':1,'uid':self.uid})