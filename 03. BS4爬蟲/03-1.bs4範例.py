import requests
from bs4 import BeautifulSoup

 # 要抓取的網址
url = 'https://tomtsun.github.io/Simple_Web/'
list_req = requests.get(url)
#將整個網站的程式碼爬下來
soup = BeautifulSoup(list_req.content, "html.parser")
#找到th這個標籤
getTitle= soup.find('div').text #只抓到第一個<h3>
print(getTitle)
getAllTitle= soup.findAll('h3') #抓到很多個li

soup.find_all('div', {'id':'container'}) #特別指定'id':'container'

a = soup.find('a', {'href': 'class3.html'})
a.find('h3')

