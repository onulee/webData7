import requests  # url정보
from bs4 import BeautifulSoup # html정보 - lxml,html-parser
from selenium import webdriver
import time
import os
import csv

# 3. 파일 불러오기
with open("gmarket1.html","r",encoding="utf8") as f:
    soup = BeautifulSoup(f,"lxml")

ul = soup.find("ul",{"class":"list__best"})
max_price = 0  # 최고가격
lis = ul.find_all("li")
f = open("gmarket.csv","w",encoding="utf-8-sig",newline="")
writer = csv.writer(f)
writer.writerow(['순위','링크','제목','가격'])
# 10개 출력
for li in lis:
    try:
        rank = li.find("span",{"class":"box__label-rank"}).text.strip()
        link = "http:"+li.find("img")['src']
        p_title = li.find("p",{"class":"box__item-title"}).text.strip()
        price_original = li.find("div",{"class":"box__price-seller"})
        price = int(price_original.find("span",{"class":"text text__value"}).text.strip().replace(",",""))
        writer.writerow([rank,link,p_title,price])
        print(rank)
        print(link)
        print(p_title)
        print(price)
        # 최고가만 max_price저장
        if max_price < price: 
            max_price = price
        print(price)
        print("-"*50)
    except: print("[[[  예외 처리 ]]]")
f.close()
print("최고가격 : ",max_price)    



# # 2. selenium 정보가져오기
# browser = webdriver.Chrome()
# browser.get("https://www.gmarket.co.kr/n/best?spm=gmktpc.home.0.0.1fbf486axva25P")
# time.sleep(5)
# soup = BeautifulSoup(browser.page_source,"lxml")

# # 파일저장
# with open("gmarket1.html","w",encoding="utf8") as f:
#     f.write(soup.prettify())   
# print("파일저장")



