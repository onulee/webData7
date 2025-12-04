from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup
import time
import os
import random

url = "https://nid.naver.com/nidlogin.login?mode=form&url=https://www.naver.com/"
browser = webdriver.Chrome()
# 1. naver 페이지 열기
browser.get(url)

# input데이터 넣기
input_js = '''
document.getElementById("id").value = "{id}";
document.getElementById("pw").value = "{pw}";
'''.format(id='onulee',pw="j20")

time.sleep(3)
# time.sleep(random.uniform(1,5))
# naver에서 elem 찾기해서 데이터 입력시 차단
# 자바스크립트를 사용해서 데이터 입력
browser.execute_script(input_js)
time.sleep(3)
browser.find_element(By.ID,"log.login").click()

input("대기")