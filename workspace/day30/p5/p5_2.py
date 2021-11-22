num = int(input("정수를 입력하세요 >>>"))
msg = ""
if num % 3 == 0:
    msg = "%는 3의 배수입니다." %num
else:
    msg = "%d는 3의 배수가 아닙니다." %num
    
print(msg)