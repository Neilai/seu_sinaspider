__author__ = "Neil"
__time__ = "2017/8/2 11:42"
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
browser= webdriver.Chrome(executable_path="D:/chromedriver.exe")
browser.get("http://www.weibo.com")
cook="SINAGLOBAL=7853109778370.708.1474885718073; UM_distinctid=15e548483790-07bd8ed06-722e3659-e1000-15e5484837a164; un=18478279702; wvr=6; YF-Ugrow-G0=b02489d329584fca03ad6347fc915997; SSOLoginState=1505034496; SCF=Ahvkk4EROXBPliCjihjH0S4P08I8Hpm63AdfAuNp4es5fFdcUSbq9kC3s6RyglBKCDXRaK5lIKhw_ivb4R66OFU.; SUB=_2A250sXFRDeRhGeBN6FEV8irIzjSIHXVXx-WZrDV8PUNbmtBeLRf6kW8qnpXsc3bxL2sCIKe-HLaLetDzCQ..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhSH1vf8PdSADmiufLqOmqx5JpX5KMhUgL.Foq0e0eXeoBXSKn2dJLoIp7LxKML1KBLBKnLxKqL1hnLBoMce0e0ShzXSh-R; SUHB=0Ryq-dkKkbl9aW; ALF=1536570475; YF-V5-G0=3737d4e74bd7e1b846a326489cdaf5ab; YF-Page-G0=f017d20b1081f0a1606831bba19e407b; _s_tentry=weibo.com; Apache=5552930636331.439.1505034507510; ULV=1505034508328:326:6:3:5552930636331.439.1505034507510:1505030199197; wb_cusLike_6333424458=N; WBtopGlobal_register_version=8ebe9c2598f18a02; UOR=,weibo.com,spr_web_360_hao360_weibo_t001"
a = cook.split(";")
result_dic = {}
for each in a:
    result = each.split("=")
    result_dic['name'] = result[0].strip()
    result_dic['value'] = result[1].strip()
    browser.add_cookie(result_dic)
print(browser.get_cookies())
browser.get("http://www.weibo.com")
time.sleep(20)
username=browser.find_element_by_xpath('//*[@id="loginname"]')
password=browser.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[2]/div/input')
login=browser.find_element_by_xpath('''//*[@id="pl_login_form"]/div/div[3]/div[6]/a''')
username.send_keys("1131894367@qq.com")#此处填入用户名
password.send_keys("laijingzhi")#此处填入密码
login.click()
time.sleep(15)
time.sleep(5)
cookie=browser.get_cookies()
print(cookie)
browser.get("http://www.weibo.com")
time.sleep(10)
cookie=browser.get_cookies()
cookie=browser.get_cookies()
print(cookie)
# cook={"cookie":"SINAGLOBAL=7853109778370.708.1474885718073; UM_distinctid=15aa30569f60-01c776242-722e3659-e1000-15aa3056a03e1; wb_cmtLike_2613164393=1; wb_publish_fist100_2613164393=1; wvr=6; YF-Ugrow-G0=56862bac2f6bf97368b95873bc687eef; login_sid_t=d4c21b9e162f334f37d349b18dff4d1f; YF-V5-G0=e6f12d86f222067e0079d729f0a701bc; _s_tentry=-; UOR=,weibo.com,spr_web_360_hao360_weibo_t001; Apache=3913146175909.7876.1501744175114; ULV=1501744175125:300:14:14:3913146175909.7876.1501744175114:1501741231638; SSOLoginState=1501744222; SCF=Ahvkk4EROXBPliCjihjH0S4P08I8Hpm63AdfAuNp4es5ekQcjJBYFeU-H56cPMaSIQbcBnvIvGGTj1r6UBxnVZo.; SUB=_2A250hrwPDeRhGeBN6FEV8irIzjSIHXVX9arHrDV8PUNbmtBeLRnjkW87KXzlMHCLYaFFWeKjku2j2TfMUw..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhSH1vf8PdSADmiufLqOmqx5JpX5K2hUgL.Foq0e0eXeoBXSKn2dJLoIp7LxKML1KBLBKnLxKqL1hnLBoMce0e0ShzXSh-R; SUHB=09P9j9kwSkQglk; ALF=1533280220; un=18478279702; WBStorage=0c663978e8e51f06|undefined; YF-Page-G0=23b9d9eac864b0d725a27007679967df; WBtopGlobal_register_version=3ad0aefd8e735ac0"}
# response=requests.get('http://weibo.com/aj/v6/comment/big?ajwvr=6&id=4136476495048061&page=1&filter=all',cookies=cook)
# # browser.get('http://weibo.com/p/1006053261134763/home?profile_ftype=1&is_all=1#_0')
# # while 1 :
# #     pre=browser.execute_script("return document.body.scrollHeight;")
# #     browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# #     time.sleep(3)
# #     cur=browser.execute_script("return document.body.scrollHeight;")
# #     if cur==pre:
# #         break
# # s="data=\"mid=4136633328668807&src=%2F%2Fpromote.vip.weibo.com%2Fpromoteadvance%3Fdai_tou%3Dpc_main_01%26touid%3D3164957712%26mid%3D4136633328668807&title=推"
# # result=re.search(r'mid=(\d*)',s)
# # print(result.group(1))
# result=json.loads(response.text)
# soup=BeautifulSoup(result['data']['html'])
# print(soup.html)
# {'domain': '.weibo.com', 'httpOnly': False, 'name': 'SSOLoginState', 'path': '/', 'secure': False, 'value': '1501862853'}, {'domain': '.weibo.com', 'httpOnly': False, 'name': 'login_sid_t', 'path': '/', 'secure': False, 'value': 'a53f1e90e455b91aeda2a96525e473b3'}, {'domain': 'weibo.com', 'httpOnly': False, 'name': 'YF-Ugrow-G0', 'path': '/', 'secure': False, 'value': '56862bac2f6bf97368b95873bc687eef'}, {'domain': '.weibo.com', 'expiry': 1532966799, 'httpOnly': False, 'name': 'ULV', 'path': '/', 'secure': False, 'value': '1501862799286:1:1:1:6878283419456.661.1501862799258:'}, {'domain': 'weibo.com', 'httpOnly': False, 'name': 'YF-V5-G0', 'path': '/', 'secure': False, 'value': '3d0866500b190395de868745b0875841'}, {'domain': 'weibo.com', 'expiry': 1501863393, 'httpOnly': False, 'name': 'WBStorage', 'path': '/', 'secure': False, 'value': '0c663978e8e51f06|undefined'}, {'domain': 'weibo.com', 'httpOnly': False, 'name': 'YF-Page-G0', 'path': '/', 'secure': False, 'value': 'd0adfff33b42523753dc3806dc660aa7'}, {'domain': '.weibo.com', 'httpOnly': False, 'name': '_s_tentry', 'path': '/', 'secure': False, 'value': '-'}, {'domain': '.weibo.com', 'expiry': 1817222799, 'httpOnly': False, 'name': 'SINAGLOBAL', 'path': '/', 'secure': False, 'value': '6878283419456.661.1501862799258'}, {'domain': '.weibo.com', 'httpOnly': False, 'name': 'Apache', 'path': '/', 'secure': False, 'value': '6878283419456.661.1501862799258'}, {'domain': '.weibo.com', 'expiry': 1817222812.153159, 'httpOnly': True, 'name': 'SCF', 'path': '/', 'secure': False, 'value': 'Aj2vdh2rn0V4nd9hFwmjnFx4cOn0IQiT4z8-d4qTkofj4X7_FAkDFr0ZwvJi4WkJG5DHuEd2qNMe7tqho2rGAj8.'}, {'domain': '.weibo.com', 'httpOnly': True, 'name': 'SUB', 'path': '/', 'secure': False, 'value': '_2A250gOuWDeRhGeRI6lEQ9irPwj-IHXVX9FperDV8PUNbmtBeLUT6kW-aLPjBTizrKTfJriOHJJg45pUTPw..'}, {'domain': '.weibo.com', 'expiry': 1533398812.153374, 'httpOnly': False, 'name': 'SUHB', 'path': '/', 'secure': False, 'value': '0nlfhfdskrrsjs'}, {'domain': '.weibo.com', 'expiry': 1533398812.153328, 'httpOnly': False, 'name': 'SUBP', 'path': '/', 'secure': False, 'value': '0033WrSXqPxfM725Ws9jqgMF55529P9D9W5QIV-4QSfrqpOpFqYT3zYh5JpX5K2hUgL.FozceKepSoB01Ke2dJLoIpjLxKnLBo-L1KqLxKqL1K-LB-eLxKBLBo.L12zt'}, {'domain': '.weibo.com', 'expiry': 1533398808.153505, 'httpOnly': False, 'name': 'ALF', 'path': '/', 'secure': False, 'value': '1533398850'}, {'domain': '.weibo.com', 'expiry': 1502726812, 'httpOnly': False, 'name': 'un', 'path': '/', 'secure': False, 'value': '1131894367@qq.com'}, {'domain': '.weibo.com', 'expiry': 1502467660.111078, 'httpOnly': False, 'name': 'wvr', 'path': '/', 'secure': False, 'value': '6'}
