count = int(input("정수 : "))
if count <= 0:
    print("다시 시도하세요")
else:
    n = 0
    while n != count:
        print("%d번째 Hello" %(n+1))
        n += 1