import requests

url = "https://www.melon.com/"
# requests url링크에 가서 html소스를 text형태로 가져옴.
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status() # 에러가 나면 프로그램을 종료
with open("agent3.html","w",encoding="utf8") as f:
    f.write(res.text)

print("파일저장완료")