import requests  # url정보
from bs4 import BeautifulSoup # html정보 - lxml,html-parser
from selenium import webdriver
import time
import os
import csv
import undetected_chromedriver as uc

## 쿠팡에서 정보 가져오기
options = uc.ChromeOptions()
options.add_argument("--no-first-run --no-service-autorun --password-store=basic")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36")

# 2. selenium 정보가져오기
url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&traceId=mipmz9on&channel=user&page=1"
browser = uc.Chrome(options=options)
browser.get(url)
time.sleep(5)
soup = BeautifulSoup(browser.page_source,"lxml")

# 파일저장
with open("coupang1.html","w",encoding="utf8") as f:
    f.write(soup.prettify())   
print("파일저장")

