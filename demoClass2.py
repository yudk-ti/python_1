#게발자 클래스를 정의 

class Developer:
    def __init__(self, name, language):
        self.name = name
        self.language = language

    def printInfo(self):
        print(f"Developer Name: {self.name}, Language: {self.language}")        

# 테스트 코드
dev1 = Developer("홍길동", "Python")        
dev1.printInfo()
dev2 = Developer("김철수", "JavaScript")    
dev2.printInfo()        


