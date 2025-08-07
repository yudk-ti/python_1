#DemoForm.py
#DemoForm.ui(화면) + DemoForm.py(로직) 

import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic   

#디자인한 파일을 로딩
form_class = uic.loadUiType("0807/DemoForm.ui")[0]

#DeoForm 클래스 정의
# class DemoForm(QMainWindow, form_class):

class DemoForm(QDialog, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # UI 설정
        self.label.setText("첫번째 문자열 출력")

if __name__ == "__main__":
    app = QApplication(sys.argv)  # QApplication 객체 생성
    demoWindow = DemoForm()  # DemoForm 객체 생성
    demoWindow.show()  # 창을 화면에 표시
    app.exec_()  # 이벤트 루프 시작