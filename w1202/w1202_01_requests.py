import requests

# requests url정보를 가져옴.
# url = "http://www.naver.com"
url = "http://www.google.com"
res = requests.get(url)
# raise_for_status:에러시 종료
# status_code : 실행코드 출력, 
# requests.codes.ok : 성공코드
# print(res.status_code) # 성공 : 200
# print(requests.codes.not_found) # ok,not_found,not_modified
res.raise_for_status() # 에러시 프로그램 종료
print("응답코드 : ",res.status_code) #성공시200, 실패404,500
print(requests.codes.ok) # 성공코드 출력 : 200


# print(res.text)
