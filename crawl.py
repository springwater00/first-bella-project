from tkinter import font
from bs4 import BeautifulSoup
import urllib.request as req
from selenium.webdriver.common.keys import Keys
from notion.client import NotionClient


"""
I want to upload my crawling bible context in Notion new page automatically, but Notion doesn't provide this survice yet. 
(Uploading files and media via the Notion API -> The API currently does not support uploading new files.)
If there's someone who can upload this, please reply to me.

"""

res = req.urlopen('https://sum.su.or.kr:8888/bible/today')
soup = BeautifulSoup( res, 'html.parser' )

cate = soup.find(class_='bibleinfo_box')
title = soup.find(class_='bible_text')
today = soup.find(class_='body_list')
catetext = cate.get_text().strip() + '\n'*5
titletext = title.get_text().strip() + '\n'*3
todaytext = today.get_text().strip()
tb = catetext + titletext + todaytext
print(tb)


# token = 'secret_xGd3IiwH49f7WjifZ1Nrh41THl6OWGOnab5WygiSVFJ'
# client = NotionClient(token_v2="d9e9fcd9b4d6bdfed5de7b3ec0cd2bd317e98be0f662eedce8335ce846e4582d721698922933a0e97299415ef47586ac8d77822ecb21c485a628f0a2131d2fd08effbb1f45562be254105794b5d2")
# list_url = 'https://www.notion.so/589edbc068ef47aaba801950826555d9?v=55ad36c284754ef28c6a062257f71939'
# collection_view = client.get_collection_view(list_url)
# new_row = collection_view.collection.add_row()

# page = client.get_block("https://www.notion.so/05b5521b16dc48b6abbb30b3273291a4?v=8576a9db79da4d958a520b73d6253405")
# print("The Notion title is:", page.title)



# send = req.urlopen('https://www.notion.so/2171dd5a65174e19b2436184fb0974cb?v=4ff00f2795a345b0a49df2535bda80b0')
# soup2 = BeautifulSoup( send, 'html.parser')


# print(cate.get_text().strip())
# print(today.get_text().strip())




# from fileinput import close
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.action_chains import ActionChains
# from bs4 import BeautifulSoup

# import requests
# import time

# driver = webdriver.Chrome()
# url = 'https://sum.su.or.kr:8888/bible/today'

# soup = BeautifulSoup(driver.get(url))
# time.sleep(60)

# driver.get_screenshot_as_png(soup.find_all(id='font_uparea02'))

# print(s)
# qt = soup.find(id_='font_uparea02')
# with open(str(now()),'wb') as f:
#     f.write(pic.read())




