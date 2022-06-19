from fileinput import close
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup

import requests
import time

driver = webdriver.Chrome()
url = 'https://sum.su.or.kr:8888/bible/today'

soup = BeautifulSoup(driver.get(url))
time.sleep(60)

driver.get_screenshot_as_png(soup.find_all(id='font_uparea02'))

print(s)
# qt = soup.find(id_='font_uparea02')
# with open(str(now()),'wb') as f:
#     f.write(pic.read())




