from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options() 
options.add_argument("user-data-dir=C:/Users/KOSMO/AppData/Local/Google/Chrome/User Data/Default")
options.add_argument("profile-directory=Default")

driver = webdriver.Chrome(options=options)
driver.get("https://new.land.naver.com/complexes?ms=37.538825,126.96535,15&a=APT:PRE:ABYG:JGC&e=RETAIL")

input("대기")