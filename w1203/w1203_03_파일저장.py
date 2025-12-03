import requests  # url정보
from bs4 import BeautifulSoup # html정보 - lxml,html-parser
from selenium import webdriver
import time
import os
import csv

fileName = "1.csv"
title = ["제목","평점","날짜"]
data1 = ["안녕1",9.1,"2025-01-01"]
data2 = ["안녕2",9.2,"2025-02-02"]
data3 = ["안녕3",9.3,"2025-03-03"]


# 파일 csv 저장방법
# csv파일 저장시 utf-8-sig인코딩으로 저장, newline : 줄바꿈 제거
f = open(fileName,"w",encoding="utf-8-sig",newline="")
writer = csv.writer(f)
# writerow 리스트타입으로 저장해야 함.
writer.writerow(title)
writer.writerow(data1)
writer.writerow(data2)
writer.writerow(data3)
f.close()  
print("파일저장") 