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

# 파일저장
f = open("stock.csv","w",encoding="utf-8-sig",newline="")
writer = csv.writer(f)

# 상단 타이틀 
# title = []
# for th in ths: title.append(th.text.strip())
maxup = ["",0]
for i,tr in enumerate(trs):
    if i==0:
        ths = tr.find_all("th")
        title = [th.text.strip() for th in ths]
        print(title)
        writer.writerow(title)
    else:
        tds = tr.find_all("td")
        if len(tds)>2:
            td0 = tds[0].text.strip()
            td1 = tds[1].text.strip()
            td2 = tds[2].text.strip()
            td3 = tds[3].text.strip()
            td4_1 = tds[4].find("em").text.strip() #상승,상한가,하락,하한가
            td4 = tds[4].find("span",{"class":"tah"}).text.strip()
            # 천단위삭제, int타입 변경
            price = int(td4.replace(",",""))
            if td4_1 == "상승" or td4_1 == "상한가":
                if maxup[1]<price:
                    maxup = [td1,price] # 최대상승종목,최대상승가
            td5 = tds[5].text.strip()
            td6 = tds[6].text.strip()
            td7 = tds[7].text.strip()
            td8 = tds[8].text.strip()
            td9 = tds[9].text.strip()
            td10 = tds[10].text.strip()
            td11 = tds[11].text.strip()
            writer.writerow([td0,td1,td2,td3,td4,td5,td6,td7,td8,td9,td10,td11])
            
            print(tds[0].text.strip())    
            print(tds[1].text.strip())    
            print(tds[2].text.strip())    
            print(tds[3].text.strip())    
            print(tds[4].find("em").text.strip())    
            print(tds[4].find("span",{"class":"tah"}).text.strip())    
            print(tds[5].text.strip())    
            print(tds[6].text.strip())    
            print(tds[7].text.strip())    
            print(tds[8].text.strip())    
            print(tds[9].text.strip())    
            print(tds[10].text.strip())    
            print(tds[11].text.strip()) 
            print("-"*50)   
           
f.close()
print("-"*50)
print("전일대비 최대상승종목 : ",maxup[0])
print("전일대비 상승가 : ",maxup[1])
            
   