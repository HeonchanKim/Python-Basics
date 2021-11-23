exam = [99, 78, 100, 91, 81, 85, 54, 100, 71, 50]
# min(값, 최소값) : 값은 최소값을 지켜야 한다.
score = [min(n + 5, 100) for n in exam]
print(score)