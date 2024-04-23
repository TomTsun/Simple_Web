import requests
import pandas as pd

#--- 取得歷年平均每股盈餘EPS
list_req = requests.get(
    'https://stock.wespai.com/p/69141', # 來源網址
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'}) # 封包header
tables = pd.read_html(
    list_req.content, # 將剛剛請求的結果內容，拿出來給pandas套件解析
    attrs = {"class":"display"}, # 指定屬性
    encoding = 'utf-8' # 設定編碼格式
    )[0]