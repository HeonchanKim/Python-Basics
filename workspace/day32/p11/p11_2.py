def get_average(marks):
    # print(marks.values())
    total = 0
    average = 0.0
    for i in list(marks.values()):
        total += i
    average = total / len(marks)
    return average
    
marks = {"국어" : 90, "영어" : 80, "수학" : 85}

print("평균 : %.2f" %get_average(marks))

