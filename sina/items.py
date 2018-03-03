# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
import re
import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, TakeFirst, Join
import time,datetime
def processdatetime(x):
    today=datetime.date.today()
    year=today.year
    x=x.lstrip()
    x=x.rstrip()

    result = re.search(r"(\d+)-(\d+)-(\d+) (\d+):(\d+):(\d+)", x)
    if result:
        timeStruct = time.strptime(x, "%Y-%m-%d %H:%M:%S")
        # 转换为时间戳:
        timeStamp = int(time.mktime(timeStruct))
        return timeStamp

    result = re.search(r"(\d+)秒前", x)
    if result:
        period = (datetime.datetime.now() - datetime.timedelta(seconds=int(result[1])))
        # 转换为时间戳:
        timeStamp = int(time.mktime(period.timetuple()))
        return timeStamp

    result=re.search(r"(\d+)分钟前",x)
    if result:
        period= (datetime.datetime.now() - datetime.timedelta(minutes=int(result[1])))
        #转换为时间戳:
        timeStamp = int(time.mktime(period.timetuple()))
        return timeStamp

    result=re.search(r"(\d+)小时前",x)
    if result:
        period= (datetime.datetime.now() - datetime.timedelta(hours=int(result[1])))
        #转换为时间戳:
        timeStamp = int(time.mktime(period.timetuple()))
        return timeStamp

    result=re.search(r"今天(.*)",x)
    if result:
        x=str(today)+result[1]
        timeStruct = time.strptime(str(x), "%Y-%m-%d %H:%M")
        timeStamp = int(time.mktime(timeStruct))
        return timeStamp

    result=re.search(r"昨天(.*)",x)
    if result:
        x=str(today)+result[1]
        timeStruct = time.strptime(str(x), "%Y-%m-%d %H:%M")
        timeStamp = int(time.mktime(timeStruct))-24*60*60*1000
        return timeStamp


    result=re.search(r"(\d+)月(\d+)日 (\d+):(\d+)",x)
    if result:
        x=str(year)+"年"+x
        timeStruct = time.strptime(x, "%Y年%m月%d日 %H:%M")
        timeStamp = int(time.mktime(timeStruct))
        return timeStamp

    result=re.search(r"(\d+)-(\d+)-(\d+) (\d+):(\d+)",x)
    if result:
        timeStruct = time.strptime(x,"%Y-%m-%d %H:%M")
        #转换为时间戳:
        timeStamp = int(time.mktime(timeStruct))
        return timeStamp


def processcook(cook):
    b = cook.split(";")
    result_dic = {}
    for each in b:
        each=each.strip()
        result = each.split("=")
        result_dic[result[0].strip()] = result[1].strip()
    return result_dic

def getlocation_gender_name(value):
    location=re.search(r'(\S+)/(\S+)',value).group(2)
    gender=re.search(r'(\S+)/(\S+)',value).group(1)
    name=re.search(r'(\S+)',value).group(1)
    return location,gender,name

def getnum3(value):
    result= re.search('(\d+)',value)
    return result.group(1)

def matchnum(item):
    length = len(item)
    for index in range(length):
        result=re.search(r'(\d+)',item[index])
        if result:
            item[index]=result.group(1)
        else:
            item[index]='0'
def deletespace(item):
    length=len(item)
    remain_element=[]
    for index in range(length):
        item[index]=item[index].strip()
        if item[index] and item[index]!='：':
            remain_element.append(item[index])
    return remain_element

def stripspace(item):
    length=len(item)
    for index in range(length):
        item[index]=item[index].strip()

def getnum(item):
    length=len(item)
    for index in range(length):
        if not  item[index].strip().isdigit():
            item[index]='0'

def JudgeNum(item):
    # length=len(item)
    # for index in range(length):
    flag = item.strip().isdigit()
    if not flag:
        item='0'
    # item[index] =item[index].strip()
    return item
class SinaItem4(scrapy.Item):
    fansname=scrapy.Field()
    fanslevel=scrapy.Field()
    fansparent=scrapy.Field()
    cookie = scrapy.Field()


class Sina_Item3(scrapy.Item):
    follow=scrapy.Field()
    webnum=scrapy.Field()
    fans=scrapy.Field()
    location=scrapy.Field()
    gender=scrapy.Field()
    username=scrapy.Field()
    cookie = scrapy.Field()

class SinaItem2(scrapy.Item):
    repeatnum=scrapy.Field()
    datetime=scrapy.Field()
    repeatname=scrapy.Field()
    cookie = scrapy.Field()

class SinaItem1(scrapy.Item):
    likenum=scrapy.Field()
    datetime=scrapy.Field()
    commentname=scrapy.Field()
    comment=scrapy.Field()
    cookie = scrapy.Field()

class SinaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    likenum=scrapy.Field(input_processor=MapCompose(JudgeNum))
    commentnum=scrapy.Field(input_processor=MapCompose(JudgeNum))
    repeatnum=scrapy.Field(input_processor=MapCompose(JudgeNum))
    datetime= scrapy.Field()
    cookie = scrapy.Field()
    pass

class SinaItemloader(ItemLoader):
    pass