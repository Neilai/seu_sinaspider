# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import time
from selenium import webdriver
from scrapy.http import HtmlResponse
from fake_useragent import UserAgent


class SinaSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.
    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r
        # spider.browser.get(start_requests.url)
        # return HtmlResponse(url=spider.browser.current_url, body=spider.browser.page_source, encoding="utf-8",request=start_requests)
    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


    def  process_request(self,request,spider):
        # if spider.cnt==150:
        #     time.sleep(10)
        #     spider.cnt=0
        if spider.name=='sinaspider':
            spider.browser.get(request.url)
            if spider.flag==1:
                while 1:
                    pre =spider.browser.execute_script("return document.body.scrollHeight;")
                    spider.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                    time.sleep(5)
                    cur = spider.browser.execute_script("return document.body.scrollHeight;")
                    if cur == pre:
                        break
            return HtmlResponse(url=spider.browser.current_url, body=spider.browser.page_source, encoding="utf-8",request=request)
        # if spider.name == 'sinaspider5':
        #     spider.browser.get(request.url)
        #     while 1:
        #         pre = spider.browser.execute_script("return document.body.scrollHeight;")
        #         spider.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        #         time.sleep(5)
        #         cur = spider.browser.execute_script("return document.body.scrollHeight;")
        #         if cur == pre:
        #             break
        #     return HtmlResponse(url=spider.browser.current_url, body=spider.browser.page_source, encoding="utf-8",request=request)

                # if spider.name == 'sinaspider1':
        #     if spider.flag == 0:
        #         spider.browser.get(request.url)
        #         spider.flag=1
        #         return HtmlResponse(url=spider.browser.current_url, body=spider.browser.page_source, encoding="utf-8",request=request)
ip_list=['14.21.183.198','115.56.135.72','49.81.254.36','122.194.248.115','182.41.49.29']
import random
class RandomUserAgentMiddlware(object):
    #随机更换user-agent
    def __init__(self, crawler):
        super(RandomUserAgentMiddlware, self).__init__()
        self.ua = UserAgent()
        self.ua_type = crawler.settings.get("RANDOM_UA_TYPE", "random")

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler)

    def process_request(self, request, spider):
        def get_ua():
            return getattr(self.ua, self.ua_type)
        request.headers.setdefault('User-Agent',get_ua())
        # index=random.randint(0,4)
        # request.meta["proxy"] =ip_list[index]

