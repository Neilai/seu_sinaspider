# -*- coding: utf-8 -*-
import scrapy
import time
from selenium import webdriver
from scrapy.selector import Selector
from items import SinaItem1,getnum,stripspace,deletespace,processcook
import json
import re

class Sinaspider1Spider(scrapy.Spider):
    name = 'sinaspider1'
    # allowed_domains = ['www.weibo.com']
    custom_settings = {
        'ITEM_PIPELINES': {'sina.pipelines.SinaPipeline1': 200,},
    }
    start_urls = ["http://weibo.com/3261134763/Ffztb4w7W?from=page_1006053261134763_profile&wvr=6&mod=weibotime&type=comment#_rnd1501944199917"]
    flag=0
    page=0
    cnt=1
    baseurl="http://weibo.com/aj/v6/comment/big?ajwvr=6"
    # def __init__(self):
    #
    #     pass
    def parse(self, response):
        result=json.loads(response.text)['data']['html']
        likenum=Selector(text=result).xpath("//div[@class='list_box']/div[@class='list_ul']/div[@comment_id]/div[@class='list_con']/div[contains(@class,'WB_func')]//span[@node-type='like_status']/em[2]/text()").extract()
        datetime=Selector(text=result).xpath("//div[@class='list_box']/div[@class='list_ul']/div[@comment_id]/div[@class='list_con']/div[contains(@class,'WB_func')]//div[contains(@class,'WB_from')]/text()").extract()
        comment_name = Selector(text=result).xpath("//div[@class='list_box']/div[@class='list_ul']/div[@comment_id]/div[@class='list_con']/div[@class='WB_text']/a[1]/text()").extract()
        comment_html=Selector(text=result).xpath("//div[@class='list_box']/div[@class='list_ul']/div[@comment_id]/div[@class='list_con']/div[contains(@class,'WB_text')]")
        comment=[]
        for each in comment_html:
            tmp=each.xpath('string(.)').extract()[0]
            comment.append(tmp)
        getnum(likenum)
        stripspace(comment)
        stripspace(comment_name)
        sina_item1=SinaItem1()
        sina_item1['likenum']=likenum
        sina_item1['datetime']=datetime
        sina_item1['comment']=comment
        sina_item1['comment_name']=comment_name
        yield sina_item1

    def start_requests(self):
        # yield scrapy.Request("http://weibo.com/aj/v6/comment/big?ajwvr=6&filter=all&id=4121910092307199&page=1", cookies=self.cook)
        self.cook = processcook(self.settings.get("COOKIE"))
        yield scrapy.Request("https://www.weibo.com/",cookies=self.cook,callback=self.loginsina)
    def loginsina(self,response):
        # time.sleep(10)
        # username = self.browser.find_element_by_xpath('//*[@id="loginname"]')
        # password = self.browser.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[2]/div/input')
        # login = self.browser.find_element_by_xpath('''//*[@id="pl_login_form"]/div/div[3]/div[6]/a''')
        # username.send_keys("1131894367@qq.com")  # 此处填入用户名
        # password.send_keys("laijingzhi")  # 此处填入密码
        # login.click()
        # time.sleep(2)
        # cookie=self.browser.get_cookies()

        yield scrapy.Request(self.settings.get("URL"),cookies=self.cook,dont_filter=True,callback=self.getmid)
    def getmid(self,response):
        #result=re.search(r'mid=(\d+)',response.text,re.DOTALL)
        mid='4137112691076812'
        url=self.baseurl+'&'+'id='+mid+'&'+'page=1'
        yield scrapy.Request(url,cookies=self.cook,dont_filter=True,callback=self.generate_page,meta={'mid':mid})
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
            yield scrapy.Request(url, cookies=self.cook, callback=self.parse)
            iterator = iterator + 1
