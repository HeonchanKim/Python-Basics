#%% dict 테스트
중국집 = {"자장면" : 1500, "짬뽕" : 2500}
print(len(중국집))
print(중국집["자장면"])

if "자장면" in 중국집 :
    중국집["자장면"] = 4000
print(중국집)

if "탕수육" not in 중국집 :
    중국집["탕수육"] = 9000
    
print(중국집)

# del 중국집["짬뽕"]
# print(중국집)

for i in 중국집.keys():
    print(i)
    
for i in range(len(중국집)):
    print(str(i + 1) + ". " + list(중국집.keys())[i])
    
total = 0
for i in 중국집.values():
    total += i
    
avg = total / len(중국집)

# print("평균 가격 : " + str(avg) + "원")
print("평균 가격 : %.2f원" %avg)
    
#%% dict task

# 등급을 입력받아서 학점을 출력해주는 프로그램
# 2 입력시 B학점입니다. 출력
# 1~5등급, A~F학점(E학점)

scoreDict = {}
# 0 1 2 3 4
# A B C D F
for i in range(5):
    scoreDict[i + 1] = chr(i+66) if i == 4 else chr(i+65)

# print(scoreDict)

rating = int(input("등급 : "))

for i in range(5):
    if rating == i+1:
        print(scoreDict[rating] + "학점 입니다.")
        break
    
if rating == 5:
    print("넌 소중헤")
    
    
    