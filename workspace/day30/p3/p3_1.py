numMsg1 = "첫번째 실수를 입력하세요"
numMsg2 = "두번째 실수를 입력하세요"

num1 = float(input(numMsg1))
num2 = float(input(numMsg2))

print("{n1}와 {n2}의 합은 {result}입니다.".format(n1=num1, n2=num2, result=num1+num2))
