#DemoForm2.py
#DemoForm2.ui(화면) + DemoForm2.py(로직) 

import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic   
from bs4 import BeautifulSoup
import urllib.request
import re


#디자인한 파일을 로딩 DemoForm2.ui
form_class = uic.loadUiType(r"c:\wd\0807\demoForm2.ui")[0]

#DeoForm 클래스 정의
# class DemoForm(QMainWindow, form_class):

class DemoForm(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # UI 설정
        self.label.setText("첫번째 문자열 출력")
    def firstClick(self):
        f = open('clien.txt', 'wt', encoding='utf-8')
        #페이지 처리(번호 생성)
        for i in range(0,10):
            url = "https://www.clien.net/service/board/sold?&od=T31&category=0&po=" + str(i)
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
        self.label.setText("클리앙 아이폰 글 저장 완료")
        # self.label.setText("클리앙 아이폰 글 저장 완료")

        




        self.label.setText("1빠")
    def secondClick(self):
        self.label.setText("2빠빠")
    def thirdClick(self):
        self.label.setText("3빠빠빠")


if __name__ == "__main__":
    app = QApplication(sys.argv)  # QApplication 객체 생성
    demoWindow = DemoForm()  # DemoForm 객체 생성
    demoWindow.show()  # 창을 화면에 표시
    app.exec_()  # 이벤트 루프 시작