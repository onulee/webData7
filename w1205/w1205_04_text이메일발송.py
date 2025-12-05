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
#날짜함수
from datetime import datetime


### 임시비밀번호 생성함수
def random_pw():
    arr = [ i for i in range(10)]
    ranNum = "".join(map(str,random.sample(arr,8)))
    print("임시비밀번호 : "+ranNum)
    return ranNum


#------------------------------------------------------
# [ 웹스크래핑 정보 ]

#### selenium 방법
# url = "http://www.naver.com"
# browser = webdriver.Chrome() # 창열기
# browser.get(url)
# soup = BeautifulSoup(browser.page_source,"lxml")
# with open('naver1.html','w',encoding="utf8") as f:
#     f.write(soup.prettify())

with open('naver1.html','r',encoding='utf8') as f:
    soup = BeautifulSoup(f,"lxml")

## 날짜
today = datetime.today()
now = today.strftime('%Y-%m-%d %H:%M:%S')
print(now)

## 온도/날씨
weather = soup.find("div",{"class":"DailyBoardView-module__weather_temperature___pOAGy"}).text.strip().replace(" ","").split("\n")
print(weather[0],weather[2])

today_weather = f"기온 : {weather[0]} / 날씨 : {weather[2]}"

low_temp = soup.find("span",{"class":"DailyBoardView-module__temperature_low___aC6Fe"}).text.strip().replace(" ","").split('\n')
print(low_temp[0],low_temp[2])
today_low_temp = f"{low_temp[0]} : {low_temp[2]}"

content = f'''{now}
{today_weather}
{today_low_temp}'''
print(content)
# [ 웹스크래핑 정보 끝 ]
#-----------------------------------------------

# content = f'''
# 임시비밀번호 : {random_pw()}
# '''

# 메일내용부분
msg = MIMEText(content)
msg['From'] = "onulee@naver.com" #보내는이 - 네이버 보내는 주소 naver.com
msg['To'] = "onulee@naver.com"   #받는이 - onulee74@gmail.com
msg['Subject'] = "임시비밀번호를 보내드립니다."

# 메일서버 정보
s = smtplib.SMTP("smtp.naver.com",587)
# 메일서버 접근
s.starttls()
# 메일서버 로그인
s.login("onulee@naver.com","C13M2RUDYSD9")
# 메일서버 발송 - 보내는이메일주소,받는주소,이메일내용부분
s.sendmail("onulee@naver.com","onulee@naver.com",msg.as_string())
print(msg.as_string())
# 메일 닫기
s.close()

print("이메일 발송완료")    



