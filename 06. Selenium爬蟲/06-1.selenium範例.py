from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd

# 自動下載ChromeDriver
service = ChromeService(executable_path=ChromeDriverManager().install())

# 關閉通知提醒 pip install webdriver-manager --upgrade
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
# 不載入圖片，提升爬蟲速度
# chrome_options.add_argument('blink-settings=imagesEnabled=false') 

# 開啟瀏覽器
driver = webdriver.Chrome(service=service, options=chrome_options)
# time.sleep(5) # 進一個頁面的時，給他時間去點擊

# 開啟網頁
driver.get("https://marketingliveincode.com/")
# time.sleep(5)

# 取得標題
driver.find_element(by=By.CLASS_NAME, value='navbar-brand').text
driver.find_elements(by=By.CLASS_NAME, value='navbar-brand')[0].text

# 取得大量格式化資料
title = driver.find_elements(by=By.CLASS_NAME, value='slide-text-title')
content = driver.find_elements(by=By.CLASS_NAME, value='slide-text-content') # get_attribute("textContent")
for tl, ct in zip(title, content):
    print(tl.text)
    print(ct.get_attribute("textContent")+ '\n')

#--- 完整爬蟲 ---
doit = True
# 先抓出全部資料
while doit:
    if len(driver.find_elements(by=By.XPATH, value="//*[contains(text(), '沒有更多了...筆者努力中！')]")) > 0:
        doit = False
    driver.execute_script('window.scrollBy(0,4000)') # 滾動到最下面
    # 按按鈕
    # driver.find_element(by=By.XPATH, value="//*[contains(text(), '我要看更多')]").click() # 有時會不給按
    element = driver.find_element(by=By.XPATH, value="//*[contains(text(), '我要看更多')]")
    driver.execute_script("arguments[0].click();", element)
    time.sleep(5)

# 在開始爬
title = driver.find_elements(by=By.CLASS_NAME, value='slide-text-title')
content = driver.find_elements(by=By.CLASS_NAME, value='slide-text-content') # get_attribute("textContent")
title_container = []
content_container = []
for tl, ct in zip(title, content):
    title_container.append(tl.text)
    content_container.append(ct.get_attribute("textContent"))
# 組成資料
data = pd.DataFrame({
    '標題':title_container,
    '說明':content_container
})
data.to_csv('行銷搬進大程式_所有文章.csv', index=False, encoding="utf-8-sig")