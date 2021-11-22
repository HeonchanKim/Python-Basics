# set : 집합, 중복된 원소를 담을 수 없다.
# 값의 유무 검사가 목적이다.

result = set()
msg = "희망하는 수학 여행지를 입력하세요."
result.add(input(msg))
result.add(input(msg))
result.add(input(msg))

print("조사되 수학여행지는 {}입니다.".format(result))
