# chat GPT
# 비교 대상 데이터
data = [1, 2, 3, 4, 2]

# 리스트 (list): 순서가 있고, 중복 허용
list_example = data
print("List:", list_example)

# 튜플 (tuple): 리스트와 유사하지만 불변 (immutable)
tuple_example = tuple(data)
print("Tuple:", tuple_example)

# 집합 (set): 순서가 없고, 중복을 허용하지 않음
set_example = set(data)
print("Set:", set_example)

# 딕셔너리 (dict): 키-값 쌍의 집합, 키는 유일함
dict_example = {k: f"value_{k}" for k in data}
print("Dict:", dict_example)

print("\n비교 요약:")
print(f"{'형식':<10} {'순서 유지':<10} {'중복 허용':<10} {'변경 가능':<10}")
print(f"{'List':<10} {'O':<10} {'O':<10} {'O':<10}")
print(f"{'Tuple':<10} {'O':<10} {'O':<10} {'X':<10}")
print(f"{'Set':<10} {'X':<10} {'X':<10} {'O':<10}")
print(f"{'Dict':<10} {'O (3.7+)':<10} {'X (키)':<10} {'O':<10}")
