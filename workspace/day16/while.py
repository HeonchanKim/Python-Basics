#%% while Test
# 이름 10번 출력
# cnt = 0
# while cnt != 10 :
#     print("{}. 김헌찬".format(cnt))
#     cnt += 1

#%% while Task1
qMsg = ("당신의 혈액형은?\n"
        + "1.A형\n2.B형\n3.O형\n4.AB형\n5.나가기\n"
        )

answer_a = "세심하고 거짓말을 잘 못한다."
answer_b = "거침없고 추진력이 좋다."
answer_o = "사교성이 좋다."
answer_ab = "착하다."
errMsg = "다시 입력해주세요."
while True:
    choice = int(input(qMsg))
    result = ""
    
    if choice == 1:
        result = answer_a
    elif choice == 2:
        result = answer_b
    elif choice == 3:
        result = answer_o
    elif choice == 4:
        result = answer_ab
    elif choice == 5:
        break
    else :
        result = errMsg
    
    print(result)

#%% while Task2 
qMsg = "다음 중 프로그래밍 언어가 아닌 것은?"
choiceMsg = "1. JAVA\n2. 파이썬\n3. C언어\n4. 망둥어\n"
choice = int(input(qMsg + "\n" + choiceMsg))
answer = 4

while result != "정답!":
    if choice == answer:
        result = "정답!"
    elif choice >= 1 and choice <= 4 :
        result = "오답"
    else :
        result = "다시 시도해주세요"
    print(result)

