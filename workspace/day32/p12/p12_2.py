import random as r
import time

answer = r.randint(1, 100)

print("UpDown게임을 시작합니다.")
start = time.time()

while True:
    n = int(input("어떤 값일까요? >>> "))
    
    if answer == n:
        print("정답입니다.")
        break
    elif answer < n:
        print("Down")
    else:
        print("Up")
end = time.time()

elapse = end - start
print("%d초만에 성공!" %elapse)