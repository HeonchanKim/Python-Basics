exam = []
print("점수를 입력하세요.")
print("더 이상 입력할 점수가 없으면 음수를 입력하세요.")
while True:
    score = int(input("점수 입력>>>"))
    if score < 0:
        break
    exam.append(score)
    
avg = sum(exam) / len(exam)
maxValue = max(exam)
minValue = min(exam)

print("평균 = %.2f, 최대 = %d, 최소 = %d " %(avg, maxValue, minValue))