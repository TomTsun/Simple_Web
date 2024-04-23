import requests
from bs4 import BeautifulSoup

stock='2002'
 # 要抓取的網址
#url = 'https://tw.stock.yahoo.com/quote/' + stock 
# url = f"https://tw.stock.yahoo.com/quote/{stock}/profile"
url = "https://tw.stock.yahoo.com/news/"

#請求網站
list_req = requests.get(url)
#將整個網站的程式碼爬下來
soup = BeautifulSoup(list_req.content, "html.parser")

len(soup.find_all('span')) # 檢測是否可以用這個標籤抓取資料

# get1 = soup.find('div', {'id':'main-0-QuoteHeader-Proxy'})
# get1.find_all('span')[2].text
#<div class="grid-item item-span-6 break-mobile"><div class="D(f) Ai(fs) H(100%) Fz(16px) Bxz(bb) Bdbw(1px) Bdbs(s) Bdc($bd-primary-divider) Lh(1.5)"><span class="As(st) Bxz(bb) Pstart(12px) Py(8px) Bgc($c-gray-hair) C($c-primary-text) Flx(n) W(104px) W(120px)--mobile W(152px)--wide Miw(u) Pend(12px) Mend(0)"><span>股本</span></span><div class="Py(8px) Pstart(12px) Bxz(bb)">157,731,289,960</div></div></div>
len(soup.find_all('div', {'class':'categoryModuleWrapper'}))

get2 = soup.find_all('div', {'class':'categoryModuleWrapper'})
result = get2[0].find_all('a')
result[2].text
# for i in range(len(get2)):
#     if '股本' in get2[i].text:
#         print(get2[i].text)

# for i in soup.find_all('div', {'class':'grid-item item-span-6 break-mobile'}):
#     print(i.text)

get3 = soup.find_all('div', {'id':'main-0-Hero-Proxy'})
get3.find('a')\

get4= soup.find_all('div', {'class':'categoryModuleWrapper'})
get4[0].text
