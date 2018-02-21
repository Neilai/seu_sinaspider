# 新浪微博爬虫
### 个人微博的爬取

采用了selenium动态抓取的策略（电脑版），需要在settings.py中修改COOKIE和想爬人的URL。

```
scrapy crawl sinaspider
```

### 单条微博评论的爬取

需要在settings.py中修改COOKIE和想爬微博的URL（电脑版），会抓取评论人，评论，评论日期等数据

```python
scrapy crawl sinaspider1
```

###单条微博转发的爬取

需要在settings.py中修改COOKIE和想爬微博的URL（电脑版），会抓取转发人，转发日期等数据

```
scrapy crawl sinaspider2
```

### 粉丝数据的抓取

由于微博的粉丝保护机制，只能爬取3000左右的粉丝数而且提供的cookie必须是电脑版的cookie,URL配置为该用户独有的ID。