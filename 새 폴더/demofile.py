#demofile.py
# f = open('c:\\wirj\\test.txt', 'wt', encoding='utf-8')      
# f.write('첫번째\n두번째\n세번째\n')
# f.close()


##파일 읽기(raw string notation)
## f= open(r'c:\work\test.txt', 'rt', encoding='utf-8')
## no back slash
# f = open('c:\\work\\test.txt', 'rt', encoding='utf-8')
## print(f.readline())  # 한 줄 읽기
# print(f.read())  # 파일 전체를 읽음
# f.close()   


# 문자열 처리
strA = " 파이썬은 강력함 "
strB = "python is very powerful"

print(len(strA))  # 문자열 길이
print(len(strB))
print(strB.capitalize())  # 첫 글자 대문자
print(strB.upper())  # 모두 대문자
print("MBC2580".isalnum())  # 알파벳과 숫자로만 구성되어 있는지 확인
print("2580".isdecimal())  # 숫자로만 구성되어 있는지 확인
data = "<<< sapm and ham >>>"
result = data.strip()  # 양쪽 공백 제거
#result = data.strip("<>")  # 양쪽 공백 제거
print(data)
print(result)

result2 = result.replace("spam", "spam and ham")  # 문자열 치환
print(result2)  
lst = result2.split()  # 공백을 기준으로 문자열 분리
print(lst)  # ['sapm', 'and', 'ham']
print(":)".join(lst))  # 리스트를 문자열로 합치기


