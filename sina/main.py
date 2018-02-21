__author__ = "Neil"
__time__ = "2017/8/2 13:14"
from scrapy.cmdline import execute
import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
execute(['scrapy','crawl','sinaspider3'])
