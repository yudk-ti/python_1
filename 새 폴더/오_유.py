from bs4 import BeautifulSoup
import urllib.request
import re



f = open('clien.txt', 'wt', encoding='utf-8')
#페이지 처리(번호 생성)

hdr = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
f = open('todayhumor.txt', 'wt', encoding='utf-8')
for n in range(1,11):
    url = "https://www.todayhumor.co.kr/board/list.php?table=bestofbest&page=" + str(n)
    #print(data)
 #   req = urllib.request.Request(data, headers = hdr)

#한글이 깨지는 경우
    data = urllib.request.urlopen(url).read()  # URL에서 HTML 데이터 읽기
    page = data.decode('utf-8', 'ignore')  # UTF-8로 디코딩
    soup = BeautifulSoup(page, 'html.parser')       
    list = soup.find_all('td', attrs={'class': 'subjrct'})
    for tag in list:
        try:
            # 내부에 <a> 태그가 있는 경우
            title = tag.find('a').text.strip()  # 문자열 양쪽 공백 제거
            if re.search('한국', title):
                 print(title)
                 f.write(title + '\n')  
           
        except:
                pass
        
# <td class="subject"><a href="/board/view.php">원숭이를 사는 사업가</a><span class="list_memo_count_span"> [17]</span>  <span style="margin-left:4px;"><img src="https://www.todayhumor.co.kr/board/images/list_icon_photo.gif" style="vertical-align:middle; margin-bottom:1px;"> </span><img src="https://www.todayhumor.co.kr/board/images/list_icon_shovel.gif?2" alt="펌글" style="margin-right:3px;top:2px;position:relative"> </td>

f.close()  # 파일 닫기