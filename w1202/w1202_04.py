import requests

url = "http://www.naver.com"
# requests url링크에 가서 html소스를 text형태로 가져옴.
res = requests.get(url)
res.raise_for_status() # 에러가 나면 프로그램을 종료
# print(res.status_code) # 성공 : 200
# print(requests.codes.not_found) # ok,not_found,not_modified

print(res.text)