import requests  # url정보
from bs4 import BeautifulSoup # html정보 - lxml,html-parser
from selenium import webdriver
import time
import os
import csv

# 1. 파일 불러오기
with open("yeogi.html","r",encoding="utf8") as f:
    soup = BeautifulSoup(f,"lxml")

div = soup.find("div",{"class":"css-1jiha5s"})
ds = div.find_all("div",{"class":"gc-thumbnail-type-seller-card-wrapper css-1u8qly9"})
img = ds[0].img["src"]
print(img)
title = ds[0].find("h3",{"class":"gc-thumbnail-type-seller-card-title css-1gxx2ac"}).text.strip()
print(title)
rating = float(ds[0].find("span",{"class":"css-9ml4lz"}).text.strip())
print(rating)
ratingCount = int(ds[0].find("span",{"class":"css-oj6onp"}).text.strip().split(" ")[0].strip().replace(",",""))
print(ratingCount)
price = int(ds[0].find("span",{"class":"css-5r5920"}).text.strip().replace(",",""))
print(price)


# 이미지 링크 가져오기
# img = ds[0].img["srcset"]
# print(img)
# print("-"*50)
# print(img.find("webp")+len("webp"))
# print("-"*50)
# print(img[:img.find("webp")+len("webp")])





# # 2. selenium 정보가져오기
# browser = webdriver.Chrome()
# browser.get("https://www.yeogi.com/domestic-accommodations?keyword=%EA%B0%95%EB%A6%89&personal=2&checkIn=2025-12-26&checkOut=2025-12-28&sortType=RECOMMEND&category=2")
# time.sleep(7)
# soup = BeautifulSoup(browser.page_source,"lxml")

# # 파일저장
# with open("yeogi.html","w",encoding="utf8") as f:
#     f.write(soup.prettify())
# print("파일저장")