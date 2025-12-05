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
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.base import MIMEBase
from email import encoders
#날짜함수
from datetime import datetime
# 마우스 제어
import pyautogui
import undetected_chromedriver as uc

# 상단 Chrome이 자동화된 테스트 소프트웨어에 의해 제어되고 있습니다 제거
options = uc.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
)
#### selenium 방법
browser = webdriver.Chrome(options=options) # 창열기
time.sleep(2)
browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": """
        Object.defineProperty(navigator, 'webdriver', {
          get: () => undefined
        })
    """
})
browser.maximize_window() # 최대창 확대
time.sleep(2)
url = "https://new.land.naver.com/complexes?ms=37.538825,126.96535,15&a=APT:PRE:ABYG:JGC&e=RETAIL"
browser.get(url)

input("대기")
