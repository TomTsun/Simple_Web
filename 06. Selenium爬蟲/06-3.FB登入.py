from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
    
useEmail = '帳號'
usePass = '密碼'

# 自動下載ChromeDriver
service = ChromeService(executable_path=ChromeDriverManager().install())

# 關閉通知提醒
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)

# 開啟瀏覽器
driver = webdriver.Chrome(service=service, chrome_options=chrome_options)
time.sleep(5)

# 開啟網頁
driver.get("http://www.facebook.com")
time.sleep(3)

driver.find_element(by=By.ID, value='email').send_keys(useEmail) # 輸入帳號
time.sleep(3)
driver.find_element(by=By.ID, value='pass').send_keys(usePass) # 輸入密碼
time.sleep(1)
driver.find_element(by=By.NAME, value='login').click() # 按下登入