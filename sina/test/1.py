a="UM_distinctid=15c07943354c8-0e8acba75299ea-5b412f19-e1000-15c07943356a0; SINAGLOBAL=6923444749677.232.1494775774189; UOR=www.baidu.com,vdisk.weibo.com,qiusuoge.com; un=1131894367@qq.com; wvr=6; YF-Ugrow-G0=9642b0b34b4c0d569ed7a372f8823a8e; SSOLoginState=1505045240; SCF=Au-0ncqPEUka5K9GGf6OW24CTp2jGe8nx00amFHVfbUvpaCpu3nNeUgmEVbXfRp96ADREj5eN8oltX8f9jWCCmc.; SUB=_2A250sVqoDeRhGeRI6lEQ9irPwj-IHXVXx8tgrDV8PUNbmtBeLUbZkW8gCo_rJWtOQJkCm_OY9Q4uqHao8g..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5QIV-4QSfrqpOpFqYT3zYh5JpX5KMhUgL.FozceKepSoB01Ke2dJLoIpjLxKnLBo-L1KqLxKqL1K-LB-eLxKBLBo.L12zt; SUHB=0nlfhfdskrrsjs; ALF=1536581239; YF-V5-G0=572595c78566a84019ac3c65c1e95574; wb_cusLike_2613164393=N; _s_tentry=-; Apache=7722360909998.964.1505045240583; YF-Page-G0=e44a6a701dd9c412116754ca0e3c82c3; ULV=1505045240652:13:3:3:7722360909998.964.1505045240583:1505034645183"
b=a.split(";")
result_dic={}
for each in b:
    result=each.split("=")
    result_dic[result[0].strip()]=result[1].strip()
print(result_dic)
# b=a.split(";")
# result_dic={}
# for each in b:
#     result=each.split("=")
#     result_dic['name']=result[0]
#     result_dic['value']=result[1]
# print(result_dic)