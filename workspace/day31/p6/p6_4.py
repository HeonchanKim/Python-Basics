numSet = set()
num = 0
while len(numSet) < 5:
    num = int(input("0~9사이의 정수 : "))
    numSet.add(num)
    
print("모두 입력되었습니다.")
print("입력된 값은 {}입니다.".format(numSet))