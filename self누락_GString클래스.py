#전역변수

strName = "Not Class Member"

class DemoString:
    def __init__(self):
        #인스턴스 멤버변수
        self.strName = "" 
    def set(self, msg):
        self.strName = msg
    def print(self):
        print(self.strName)
        #print(strName) 버그

d = DemoString()
d.set("First Message")
d.print()
