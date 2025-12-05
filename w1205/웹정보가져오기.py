import time
import os
import random
# 웹스크래핑
import requests
from bs4 import BeautifulSoup
# selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
# 이메일발송라이브러리
import smtplib
from email.mime.text import MIMEText

### 웹스크래핑
url = "http://www.naver.com"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36"}
res=requests.get(url,headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text,"lxml")

#### selenium 방법
url = "http://www.naver.com"
browser = webdriver.Chrome() # 창열기
browser.get(url)
soup = BeautifulSoup(browser.page_source,"lxml")