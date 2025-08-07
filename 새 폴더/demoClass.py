#1) Class 정의
class Person:
    #초기화 method
    def __init__(self):
        self.name = "default name"
    def print(self):
        print("My name is {0}" .format(self.name))

#2) 인스턴스 생성
p1 = Person()
#3) method 호출 

p1.print()