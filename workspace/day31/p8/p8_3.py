key = 'qwerty'

count = 0

while True:
    if count == 5:
        print("입력 횟수 초과")
        break
    pw = input("비밀번호 : ")
    if pw == key:
        print("비밀번호를 맞췄습니다.")
        break
    count += 1
        
        