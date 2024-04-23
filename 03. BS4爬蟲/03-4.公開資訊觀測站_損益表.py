import requests
from bs4 import BeautifulSoup
import pandas as pd

stock='2002'
 # 要抓取的網址
url = 'https://mops.twse.com.tw/mops/web/t164sb04'

#請求網站
list_req = requests.post(url, data={
    'encodeURIComponent': '1',
    'step': '1',
    'firstin': '1',
    'off': '1',
    'queryName': 'co_id',
    'inpuType': 'co_id',
    'TYPEK': 'all',
    'isnew': 'true',
    'co_id': stock
})
#將整個網站的程式碼爬下來
soup = BeautifulSoup(list_req.content, "html.parser")
# 取得報表特定部分
getTable = str(soup.find('div', {'id':'table01'}))

getdata=pd.read_html( getTable , header = 0)