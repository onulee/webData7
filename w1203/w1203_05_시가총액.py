import requests  # url정보
from bs4 import BeautifulSoup # html정보 - lxml,html-parser
from selenium import webdriver
import time
import os
import csv

# 1. requests 정보가져오기
url = "https://finance.naver.com/sise/lastsearch2.naver"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
soup = BeautifulSoup(res.text,"lxml")
box_type = soup.find("div",{"class":"box_type_l"}) 
trs = box_type.find_all("tr")
ths = trs[0].find_all("th")
print(ths[0].text.strip())
# 상단 타이틀 
title = [th.text.strip() for th in ths]
print(title)

# title = []
# for th in ths: title.append(th.text.strip())


# stock.csv -> 파일저장