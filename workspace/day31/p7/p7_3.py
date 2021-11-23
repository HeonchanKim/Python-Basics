cnt = int(input("몇 개의 과일을 보관할까요?"))
fruitList = []
for i in range(cnt):
    fruitList.append(input("%d 번째 과일을 입력하세요 >>> " %(i+1)))

print(fruitList)
