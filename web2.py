#web2.py

from bs4 import BeautifulSoup
import urllib.request
import re



#파일로 저장
f = open('clien.txt', 'wt', encoding='utf-8')
#페이지 처리(번호 생성)

for i in range(0,10):
    url = "https://www.clien.net/service/board/sold?&od=T31&category=0&po=" + str(i)
    #print(url)


    print(url)
#함수 체인(method chain)
    data = urllib.request.urlopen(url).read()  # URL에서 HTML 데이터 읽기


    soup = BeautifulSoup(data, 'html.parser')       
    for tag in soup.find_all('span', attrs={'data-role': 'list-title-text'}):
         title = tag.text.strip()  # 문자열 양쪽 공백 제거
         if re.search('아이폰', title):
            print(title)
            f.write(title + '\n')  # 파일에 제목 쓰기

f.close()  # 파일 닫기

    # 페이지를 로딩
	# <span class="subject_fixed" data-role="list-title-text" title="아이폰 13미니 256 팝니다">
	# 	아이폰 13미니 256 팝니다
    # </span>

