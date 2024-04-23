import requests
import json

 # 要抓取的網址
url = 'https://trends.google.com.tw/trends/api/dailytrends?hl=zh-TW&tz=-480&geo=TW&hl=zh-TW&ns=15'
#請求網站
list_req = requests.get(url)
gettext = list_req.content
#將整個網站的程式碼爬下來
getdata = json.loads(gettext[6:])