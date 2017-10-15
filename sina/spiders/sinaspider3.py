# -*- coding: utf-8 -*-
import scrapy
import json
import re
from items import  getnum3,getlocation_gender_name,Sina_Item3
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
    cook = {'domain': '.weibo.cn', 'httpOnly': False, 'name': 'SSOLoginState', 'path': '/', 'secure': False, 'value': '1501868580'}, {'domain': '.weibo.cn', 'expiry': 1504460537.575221, 'httpOnly': False, 'name': 'ALF', 'path': '/', 'secure': False, 'value': '1504460579'}, {'domain': '.weibo.cn', 'expiry': 1533404538.458676, 'httpOnly': False, 'name': 'SUHB', 'path': '/', 'secure': False, 'value': '0vJ5gK-4DOqoxn'}, {'domain': '.weibo.cn', 'expiry': 1533404538.458599, 'httpOnly': False, 'name': 'SUBP', 'path': '/', 'secure': False, 'value': '0033WrSXqPxfM725Ws9jqgMF55529P9D9W5QIV-4QSfrqpOpFqYT3zYh5JpX5o2p5NHD95QESo20eKqXe0.0Ws4Dqcjdi--Ri-zfiK.ci--ciK.fi-8hi--Xi-z4iKyF'}, {'domain': '.weibo.cn', 'expiry': 1817228538.4583793, 'httpOnly': True, 'name': 'SCF', 'path': '/', 'secure': False, 'value': 'Amca3i5TurarlUkR7K68Mpj_5LTl8wGOooymms7S0P0_eNp1WTidM3opQhdqM2NyXDfbENYm_XReGduuzTxc4Mk.'}, {'domain': '.weibo.cn', 'expiry': 1501869141.563377, 'httpOnly': True, 'name': 'M_WEIBOCN_PARAMS', 'path': '/', 'secure': False, 'value': 'luicode%3D20000174%26uicode%3D20000174%26featurecode%3D20000320%26fid%3Dhotword'}, {'domain': '.weibo.cn', 'expiry': 1533404538.458504, 'httpOnly': True, 'name': 'SUB', 'path': '/', 'secure': False, 'value': '_2A250gMJ0DeRhGeRI6lEQ9irPwj-IHXVXiu48rDV6PUJbktBeLU_8kW0GtA9FKnBPANtIlJ1TEyxglEPxAw..'}, {'domain': '.weibo.cn', 'expiry': 1504460538.716496, 'httpOnly': True, 'name': '_T_WM', 'path': '/', 'secure': False, 'value': 'ac569e4260797ed951734530fea1d779'}
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
