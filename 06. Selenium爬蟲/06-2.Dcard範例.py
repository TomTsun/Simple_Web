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
time.sleep(5)

# 開啟網頁
driver.get("https://www.dcard.tw/f/graduate_school")
time.sleep(5)

driver.execute_script('window.scrollBy(0,4000)') # 滾動到最下面