import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time

# 2. selenium 정보가져오기
# browser = webdriver.Chrome()
# browser.get("http://www.naver.com")
# time.sleep(5)
# soup = BeautifulSoup(browser.page_source,"lxml")
# print(soup.prettify())
# # 파일저장
# with open("test.html","w",encoding="utf8") as f:
#     f.write(soup.prettify())
# # 파일불러오기
# with open("test.html","r",encoding="utf8") as f:
#     BeautifulSoup(f,"lxml")


# 1. requests 정보가져오기
# url = "http://www.naver.com"
# headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36"}
# res = requests.get(url,headers=headers)
# soup = BeautifulSoup(res.text,"lxml")
# print(soup.prettify())

