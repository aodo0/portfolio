# parser.py
import requests
import os
#크롤링에 사용할 모듈 
from bs4 import BeautifulSoup
#오늘 날짜를 출력하기 위함
from datetime import datetime

# python 파일의 위치
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
#오늘 날짜 출력
now = (datetime.now()).strftime('%Y-%m-%d')

#크롤링할 웹 페이지
request =  requests.get('https://azure.microsoft.com/ko-kr/updates/')
#웹 요청을 변수 html에 담는다 
html = request.text
#웹 페이지의 내용을 parser를 이용해서 변수에 담는다
soup = BeautifulSoup(html, 'html.parser')

#HTML 코드에서 p태그 안에 들어있는 값들 중 class가 azure-nav-expand__link-desc 인 것을 필터링 한다.
TitleList = soup.find_all('p', class_ = "azure-nav-expand__link-desc")

TitleDic = [] #리스트 자료형 변수를 선언합니다.
Num = 1 #Title에 숫자를 붙여주기 위해서 초기화를 한다.
for One in TitleList: #변수 안에 있는 여러 자료들 중 text를 출력하기 위함입니다.
    #div 태그 안에 포함된 p 태그 내용을 변수 PTag에 담는다
    #PTag = One.select('div > p')
    for i in One: #one 값이 있다면 계속 반복한다.
        if 'SQL' in i.get_text(): #만약 최신 소식 중에 SQL 이 있다면 추출한다.
            dic = {'Num':Num, 'Title':i.get_text()} #(i.get_text()) #태그 속에 있는 텍스트 많을 반환하기 위해서 get_text를 적용한다
            TitleDic.append(dic) #딕셔너리 형태로 키,값이 넣어진 변수를 리스트 자료형에 담는다
            Num += 1 #Title 숫자를 세기 위해서 하나를 더한다.

#파일 생성을 위해 현재 경로와 파일 생성 이름을 변수로 넣어줍니다.
FilePath = f"{BASE_DIR}" + f"\{now}_WebCrawlerData_포트폴리오_장유지.txt"
NewFile = open(FilePath,'w')
print(TitleDic, file= NewFile)
NewFile.close()
