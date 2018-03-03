# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import MySQLdb
import MySQLdb.cursors
import redis
from items import processdatetime
class SinaPipeline(object):
    def __init__(self):

        # self.conn = MySQLdb.connect('127.0.0.1', 'root', '19971008', 'sina_spider', charset="utf8", use_unicode=True)
        # self.cursor = self.conn.cursor()

        self.myredis=r = redis.Redis(host='127.0.0.1', port=6379)
    def process_item(self, item, spider):
        # insert_sql = """
        #            insert into sina(likenum,commentnum,repeatnum,datetime)
        #            VALUES (%s, %s, %s,%s)
        #        """
        # self.cursor.execute(insert_sql, (int(item["likenum"]),int(item["commentnum"]), int(item["repeatnum"]),int(processdatetime(item["datetime"]))))
        # self.conn.commit()

        # cnt=len(item['likenum'])
        # for index in range(cnt):
        #     self.cursor.execute(insert_sql, (item["likenum"][index],item["commentnum"][index], item["repeatnum"][index],processdatetime(item["datetime"][index])))
        #     self.conn.commit()

        self.myredis.rpush(item["cookie"] + "likenum", item["likenum"])
        self.myredis.rpush(item["cookie"] + "commentnum", item["commentnum"])
        self.myredis.rpush(item["cookie"] + "datetime", processdatetime(item["datetime"]))
        self.myredis.rpush(item["cookie"] + "repeatnum", item["repeatnum"])


class SinaPipeline1(object):
    def __init__(self):
        # self.conn = MySQLdb.connect('127.0.0.1', 'root', '19971008', 'sina_spider', charset="utf8", use_unicode=True)
        # self.cursor = self.conn.cursor()

        self.myredis = r = redis.Redis(host='127.0.0.1', port=6379)
    def process_item(self, item, spider):
        # insert_sql = """
        #               insert into sina1(comment_name,likenum,comment,datetime)
        #               VALUES (%s, %s, %s,%s)
        #           """
        cnt = len(item['likenum'])
        for index in range(cnt):
            # try:
            #     self.cursor.execute(insert_sql,(item["commentname"][index], item["likenum"][index], item["comment"][index],int(processdatetime(item["datetime"][index]))))
            #     self.conn.commit()
            # except  Exception as e:
            #     print(e)
            self.myredis.rpush(item["cookie"] + "likenum1", item["likenum"][index])
            self.myredis.rpush(item["cookie"] + "comment1", item["commentnum"][index])
            self.myredis.rpush(item["cookie"] + "datetime1", item["datetime"][index])
            self.myredis.rpush(item["cookie"] + "commentname1", item["comment"][index])

class SinaPipeline2(object):
    def __init__(self):
        # self.conn = MySQLdb.connect('127.0.0.1', 'root', '19971008', 'sina_spider', charset="utf8", use_unicode=True)
        # self.cursor = self.conn.cursor()

        self.myredis = r = redis.Redis(host='127.0.0.1', port=6379)
    def process_item(self, item, spider):
        # insert_sql = """
        #               insert into sina2(repeatname,repeatnum,datetime)
        #               VALUES (%s, %s, %s)
        #           """

        cnt = len(item['repeatnum'])
        for index in range(cnt):
            # self.cursor.execute(insert_sql,(item["repeatname"][index], item["repeatnum"][index],int(processdatetime(item["datetime"][index]))))
            # self.conn.commit()

            self.myredis.rpush(item["cookie"] + "repeatnum2", item["repeatnum"][index])
            self.myredis.rpush(item["cookie"] + "datetime2", processdatetime(item["datetime"][index]))
            self.myredis.rpush(item["cookie"] + "repeatname2", item["repeatname"][index])

class SinaPipeline3(object):
    def __init__(self):
        # self.conn = MySQLdb.connect('127.0.0.1', 'root', '19971008', 'sina_spider', charset="utf8", use_unicode=True)
        # self.cursor = self.conn.cursor()

        self.myredis = r = redis.Redis(host='127.0.0.1', port=6379)
    def process_item(self, item, spider):
        # insert_sql = """
        #               insert into sina3(username,gender,location,follow,webnum,fans)
        #               VALUES (%s, %s, %s,%s, %s, %s)
        #           """
        # self.cursor.execute(insert_sql,(item["username"], item["gender"], item["location"],item["follow"],item['webnum'],item['fans']))
        # self.conn.commit()

        self.myredis.rpush(item["cookie"] + "username3", item["username"])
        self.myredis.rpush(item["cookie"] + "gender3", item["gender"])
        self.myredis.rpush(item["cookie"] + "location3", item["location"])
        self.myredis.rpush(item["cookie"] + "webnum3", item["webnum"])
        self.myredis.rpush(item["cookie"] + "fans3", item["fans"])

class SinaPipeline4(object):
    def __init__(self):
        self.conn = MySQLdb.connect('127.0.0.1', 'root', '19971008', 'sina_spider', charset="utf8", use_unicode=True)
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        insert_sql = """
                      insert into sina4(fansparent,fansname,fanslevel)
                      VALUES (%s, %s, %s)
                  """
        cnt = len(item['fanslevel'])
        for index in range(cnt):
            self.cursor.execute(insert_sql,
                                (item["fansparent"][index], item["fansname"][index], item["fanslevel"][index]))
            self.conn.commit()
        pass