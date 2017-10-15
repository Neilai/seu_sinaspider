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
    baseapi='https://m.weibo.cn/api/container/getIndex?containerid=231051_-_fans_-_3261134763&since_id='
    baseurl='https://weibo.cn/u/'
    index=18
    cnt=0
    def parse(self, response):
      dic=json.loads(response.text)
      uid = []
      if  'cards' in dic['data'].keys():
        users=dic['cards'][0]['card_group']
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
        follow=response.xpath("//div[@class='u']/div[@class='tip2']/a[2]/text()").extract()[0]
        sina_item3 =Sina_Item3()
        sina_item3['webnum']=getnum3(webnum)
        sina_item3['follow']=getnum3(follow)
        sina_item3['fans']=getnum3(fans)
        sina_item3['location'],sina_item3['gender'],sina_item3['username']=getlocation_gender_name(location_and_username)
        yield sina_item3
        pass
    def start_requests(self):
        # yield scrapy.Request("https://weibo.cn/u/2290732425",cookies=self.cook)
        self.cook = processcook(self.settings.get("COOKIE"))
        yield scrapy.Request("https://m.weibo.com/", cookies=self.cook, callback=self.loginsina)

    def loginsina(self, response):
        # time.sleep(10)
        # username = self.browser.find_element_by_xpath('//*[@id="loginname"]')
        # password = self.browser.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[2]/div/input')
        # login = self.browser.find_element_by_xpath('''//*[@id="pl_login_form"]/div/div[3]/div[6]/a''')
        # username.send_keys("1131894367@qq.com")  # 此处填入用户名
        # password.send_keys("laijingzhi")  # 此处填入密码
        # login.click()
        # time.sleep(2)
        # cookie=self.browser.get_cookies()[0]
        for url in self.start_urls:
            yield scrapy.Request(url, cookies=self.cook, callback=self.parse)
