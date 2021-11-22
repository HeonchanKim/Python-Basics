kor = int(input("국어 : "))
eng = int(input("영어 : "))
math = int(input("수학 : "))

total = kor + eng + math
avg = total / 3

result = "합격" if avg >= 80 else "불합격"
print("평균은 %.2f이고, 결과는 %s입니다." %(avg, result))