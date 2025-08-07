#2.1_data.py

strA = " 파이썬은 강력해"
strB = " python is very powerful"

print(len(strA))
print(len(strB))
print(strA[:2])
print(strA[-2:])
print(strB[:6])
print(strB[-5:])

strC = """이번에는
다중의 라인을
저장합니다."""


print(strC)


##list
print("---list format---")
lst = [10,20,30]
print(len(lst))
lst.append(40)
print(lst)
lst.remove(20)
print(lst)
lst.insert(4, "white")
print(lst)

print("---Tuple---")

tp = ( 100, 200, 300)
print(len(tp))
print(tp[1])
print(tp.index(300))


# 함수 정의

def calc(a,b):
    return a+b, a*b, a/b

# 함수를 호출
test = calc(10,2)

print(calc(10,2))
print(test)

print(len(test))
print(test[1])

print("id:%s, name:%s" % ( "yu", "유다경" ))

args = (5,6)
print(calc(*args))

print("---set형식---")
a = {1,2,2,3}
b = {3,4,4,5}
print(a)
print(b)
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))

print("---형식변환---")


c = set ((1,2,3))
print(c)
d = list(c)
d.append(10)
print(d)
e = tuple(d)
print(e)



print("---dic---")
colors = {"apple":"red", "banana":"yellow"}

colors["cherry"] = "red"
print(colors)

print(colors["apple"])
del colors["apple"]
print(colors) 


#장비 모음

device = { "iphone":5, "ipad":10, "mac":7 }
device["dell"] = 20
print(device)
device["iphone"] = 9
print(device)
del device["ipad"]
print(device)

for item in device.items():
    print(item)

for k,v in device.items():
    print(k,v)
