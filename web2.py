#web2.py

from bs4 import BeautifulSoup
import urllib.request
import re

url = "https://www.clien.net/service/board/sold"
#함수 체인(method chain)
data = urllib.request.urlopen(url).read()  # URL에서 HTML 데이터 읽기

soup = BeautifulSoup(data, 'html.parser')       
for tag in soup.find_all('span', attrs={'data-role': 'list-title-text'}):
    title = tag.text.strip()  # 문자열 양쪽 공백 제거
    print
    # 페이지를 로딩
	# <span class="subject_fixed" data-role="list-title-text" title="아이폰 13미니 256 팝니다">
	# 	아이폰 13미니 256 팝니다
    # </span>

