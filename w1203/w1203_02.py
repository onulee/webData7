import requests  # url정보
from bs4 import BeautifulSoup # html정보 - lxml,html-parser
from selenium import webdriver
import time
import os
import csv

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36"}

#url = f"https://comic.naver.com/webtoon/list?titleId=811721&page=1&sort=DESC"

# 1~3페이지까지 출력
j = 1
all_rating = 0
all_len = 0
for i in range(1,4):
    url = f"https://comic.naver.com/webtoon/list?titleId=811721&page={i}&sort=DESC"
    browser = webdriver.Chrome() # 크롬브라우저 열기
    browser.get(url)             # 페이지이동
    time.sleep(5)                # html페이지 불러오는 동안 시간 대기
    soup = BeautifulSoup(browser.page_source,"lxml")

    # 4. 파일저장
    # with open (f"naver_webtoon{i+1}.html","w",encoding="utf8") as f:
    #     f.write(soup.prettify())
    # 3. 파일 불러오기
    # with open(f"naver_webtoon{i+1}.html","r",encoding="utf8") as f:
    #     soup = BeautifulSoup(f,"lxml")

    ul = soup.find("ul",{"class":"EpisodeListList__episode_list--_N3ks"})
    lis = ul.find_all("li")
    print("개수 : ",len(lis))
    rating = 0
    
    for i,li in enumerate(lis):
        # 이미지 파일을 불러오기
        img_url = requests.get(li.find("img")['src'],headers=headers)
        os.makedirs("naver_webtoon",exist_ok=True)
        # 파일저장
        with open(f"naver_webtoon/webtoon_{j}_{i+1}.jpg","wb") as f:
            f.write(img_url.content) #content파일내용을 모두 가져오기
        
        print(li.find("img")['src'])
        print(li.find("span",{"class":"EpisodeListList__title--lfIzU"}).text.strip())
        rating += float(li.find("span",{"class":"text"}).text.strip())
        print(li.find("span",{"class":"text"}).text.strip())
        print(li.find("span",{"class":"date"}).text.strip())
        print("-"*50)
        
    j += 1    

    print("20개 평균평점 : ",f"{rating/len(lis):.2f}")    
    all_rating += rating
    all_len += len(lis)
    
# 전체평균평점
print("전체평균평점 : ",f"{all_rating/all_len:.2f}")    



# # 2. selenium 정보가져오기
# browser = webdriver.Chrome()
# browser.get("https://comic.naver.com/webtoon/list?titleId=811721&page=1&sort=DESC")
# time.sleep(5)
# soup = BeautifulSoup(browser.page_source,"lxml")

# # 파일저장
# with open("webtoon2.html","w",encoding="utf8") as f:
#     f.write(soup.prettify())
# print("파일저장")


# 1. requests 정보가져오기
# url = "https://comic.naver.com/webtoon/list?titleId=811721&page=1&sort=DESC"
# headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36"}
# res = requests.get(url,headers=headers)
# soup = BeautifulSoup(res.text,"lxml")
# print(soup.prettify())


    