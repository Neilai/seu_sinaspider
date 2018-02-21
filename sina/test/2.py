import time
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import re
import json
# header={'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0"}
# chromeOptions = webdriver.ChromeOptions()
# prefs = {"profile.managed_default_content_settings.images":2}
# chromeOptions.add_experimental_option("prefs",prefs)
browser= webdriver.PhantomJS()
browser.get("http://www.weibo.com")
print(browser)