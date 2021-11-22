car_no = input("차량번호 : ")
msg = ""

if int(car_no[-1]) % 2 == 0:
    msg = "%s는 오늘 운행이 가능합니다." %car_no
else:
    msg = "%s는 오늘 운행이 불가능합니다." %car_no
    
print(msg)
