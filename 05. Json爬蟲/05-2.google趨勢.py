import requests
import json

 # 要抓取的網址
url = 'https://www.104.com.tw/jobs/search/list?ro=2&isnew=3&kwop=7&keyword=%E5%AF%A6%E7%BF%92&expansionType=area%2Cspec%2Ccom%2Cjob%2Cwf%2Cwktm&order=7&asc=0&sr=99&rostatus=1024&page=2&mode=s&jobsource=student2020&langFlag=0&langStatus=0&recommendJob=1&hotJob=1'

header = {
    "Accept":"application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding":"gzip, deflate, br",
    "Accept-Language":"zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    "Connection":"keep-alive",
    "Cookie":"_ga=GA1.4.572441622.1696381745; luauid=118781575; _fbc=fb.2.1698202127066.IwAR0w8PlwTDdhYV5Mth58-YAZTh5KJxKW0BxfgPhJSv_s0gge5u12Dhehnzs; _fbp=fb.2.1698202127067.614367093; _hp2_id.3192618648=%7B%22userId%22%3A%224679213542068613%22%2C%22pageviewId%22%3A%222472741394662432%22%2C%22sessionId%22%3A%226065473962573054%22%2C%22identity%22%3Anull%2C%22trackerVersion%22%3A%224.0%22%7D; ACUD=7a98aba8-8a7f-4545-808e-54ddfe25db48; _ga_TTXLT7SQ8E=GS1.1.1698202604.1.1.1698202635.29.0.0; _ga=GA1.1.572441622.1696381745; c_main_rwd=0; _hjid=74d51deb-785c-498b-831b-40bef4c41399; _hjMinimizedPolls=869445; _hjSessionUser_3218023=eyJpZCI6ImMyMzZiZDdjLWQ0MTQtNTEwMi05N2ZkLWJjODEwZjkyOGE1MCIsImNyZWF0ZWQiOjE2OTgzNzI2NjI0MDMsImV4aXN0aW5nIjp0cnVlfQ==; _ga_W9X1GB1SVR=GS1.1.1698377348.7.1.1698377348.60.0.0; _ga_FJWMQR9J2K=GS1.1.1698377348.7.1.1698377348.60.0.0; _ga_WYQPBGBV8Z=GS1.4.1698377348.7.1.1698377348.60.0.0; c_job_algo_exp_poc=B; c_job_algo_exp_date_poc=F; dtCookie=v_4_srv_3_sn_BE57E8AD1A61F9FA42DEABE3ECB52E9D_perc_100000_ol_0_mul_1_app-3Aea7c4b59f27d43eb_0; c_job_view_job_info_nabi=82gak%2C2005001005%2C2002001010; job_same_ab=2; TS01e1e367=01180e452df326b981e9b5a9f76e5f3f7fd8f854077e772188258d6013bffe0cd2cfc0e08c2e99a29406c5d1602299acc27d4cbec0376614b781a41a34674914b191108c6eec0b3c38f714fe578f96cf9c17512b956c0887a05ccf58f218228a570078744f; TS016ab800=01180e452d162c9e4e29a0b83a20b1acce0b6d0de316abf1da6130b489ff93aa8c24da03d80e78f1382263d0ca9ec53e16fc03d0e08d85ed74ae1327723e18b01bfa3d1dcae003ceafb3f40f890713a791b764725c5be735442874b5ce20d62dbeeb4d5b43; __cf_bm=k_OKLj5BwlOVWZtNHFxNrFJ4wsV3vqTvYogsI7bihIw-1700900217-0-AcSGCbsBeJnoodQCZcRY0DNXJ0x03IZ4Mt2YNS5mo0kjhyc0Dgi+b2jeYPaUKqbaPqSHpuIgw9BsCItut1zolkU=; lup=118781575.4595615004580.4623532291991.1.4640712161167; lunp=4623532291991",
    "Host":"www.104.com.tw",
    "Referer":"https://www.104.com.tw/jobs/search/?keyword=%E5%AF%A6%E7%BF%92&ro=2&isnew=3&kwop=7&expansionType=area%2Cspec%2Ccom%2Cjob%2Cwf%2Cwktm&order=7&asc=0&sr=99&rostatus=1024&page=1&mode=s&langFlag=0&langStatus=0&jobsource=student2020",
    "Sec-Ch-Ua":'"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    "Sec-Ch-Ua-Mobile":'?1',
    "Sec-Ch-Ua-Platform":'"Android"',
    "Sec-Fetch-Dest":"empty",
    "Sec-Fetch-Mode":"cors",
    "Sec-Fetch-Site":"same-origin",
    "User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Mobile Safari/537.36",
    "X-Requested-With":"XMLHttpRequest"
}
dataa = {    
    "ro":"2",
    "isnew":"3",
    "kwop":"7",
    "keyword":"實習",
    "expansionType":"area,spec,com,job,wf,wktm",
    "order":"7",
    "asc":"0",
    "sr":"99",
    "rostatus":"1024",
    "page":"2",
    "mode":"s",
    "jobsource":"student2020",
    "langFlag":"0",
    "langStatus":"0",
    "recommendJob":"1",
    "hotJob":"1"
}

#請求網站
list_req = requests.get(url, headers =header, data= dataa)
gettext = list_req.content
#將整個網站的程式碼爬下來
getdata = json.loads(gettext)