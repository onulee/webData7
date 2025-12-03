import requests  # url정보
from bs4 import BeautifulSoup # html정보 - lxml,html-parser
from selenium import webdriver
import time
import os
import csv
import undetected_chromedriver as uc

# 1. 파일 불러오기
with open("coupang1.html","r",encoding="utf8") as f:
    soup = BeautifulSoup(f,"lxml")

ul = soup.find("ul",{"id":"product-list"})
lis = ul.find_all("li")

# 노트북 가격 1100000이하
# 평점 4.5 이상
# 후기 500 이상만 출력하시오.
print("[ 노트북 추천 ]")
for i,li in enumerate(lis):
    print(f"{i+1}.") 
    img_url = li.img['src']
    title = li.find("div",{"class":"ProductUnit_productNameV2__cV9cw"}).text.strip()
    price1 = li.find("div",{"class":"custom-oos fw-text-[20px]/[24px] fw-font-bold fw-mr-[4px] fw-text-red-700"})
    price2 = li.find("div",{"class":"custom-oos fw-text-[20px]/[24px] fw-font-bold fw-mr-[4px] fw-text-bluegray-900"})
    price3 = li.find("div",{"class":"custom-oos fw-text-[20px]/[24px] fw-font-bold fw-mr-[4px] fw-text-bluegray-400"})
    price4 = li.find("strong",{"class":"Price_priceValue__A4KOr"})
    if price1: # None인지 확인
        price = int(price1.text.strip()[:-1].replace(",",""))
    elif price2:
        price = int(price2.text.strip()[:-1].replace(",",""))
    elif price3:
        price = int(price3.text.strip()[:-1].replace(",",""))
    else:
        price = int(price4.text.strip()[:-1].replace(",",""))
    
    rating = float(li.find("div",{"class":"ProductRating_star__RGSlV"}).text.strip())
    ratingCount = li.find("span",{"class":"ProductRating_ratingCount__R0Vhz"})
    ratingCount = int(ratingCount.text.strip()[1:-1])
    
    if price <=1100000 and rating>=4.5 and ratingCount>=500:
        print(img_url)
        print(title)
        print(price)
        print(rating)
        print(ratingCount)
        print("-"*50)
    else:
        print("[ 조건에 맞지 않음. ]") 
    
    
    

# for i,li in enumerate(lis):
#     print(f"{i+1}.") 
#     try:
#         price = int(li.find("div",{"class":"custom-oos fw-text-[20px]/[24px] fw-font-bold fw-mr-[4px] fw-text-bluegray-900"}).text.strip()[:-1].replace(",",""))
#         rating = float(li.find("div",{"class":"ProductRating_star__RGSlV"}).text.strip())
#         ratingCount = int(li.find("span",{"class":"ProductRating_ratingCount__R0Vhz"}).text.strip()[1:-1])
#         if price <=1100000 and rating>=4.5 and ratingCount>=500:
#             print(li.img['src'])
#             print(li.find("div",{"class":"ProductUnit_productNameV2__cV9cw"}).text.strip())
#             print(price)
#             print(rating)
#             print(ratingCount)
#             print("-"*50)
#         else:
#             print("[ 조건에 맞지 않음. ]")    
#     except:
#         print("[ 예외 처리 ]")

### 쿠팡에서 정보 가져오기
# options = uc.ChromeOptions()
# options.add_argument("--no-first-run --no-service-autorun --password-store=basic")
# options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36")

# # 2. selenium 정보가져오기
# url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&traceId=mipmz9on&channel=user&page=1"
# browser = uc.Chrome(options=options)
# browser.get(url)
# time.sleep(5)
# soup = BeautifulSoup(browser.page_source,"lxml")

# # 파일저장
# with open("coupang1.html","w",encoding="utf8") as f:
#     f.write(soup.prettify())   
# print("파일저장")

