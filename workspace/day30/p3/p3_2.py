days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
month = int(input("1~12사이의 월을 입력하세요"))
print("%d월은 %d일까지 있습니다." %(month, days[month-1]))