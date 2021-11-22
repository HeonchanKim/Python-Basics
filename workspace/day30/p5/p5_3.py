n1 = int(input("정수1 : "))
n2 = int(input("정수2 : "))
n3 = int(input("정수3 : "))

msg = ""

if n1 >= n2 and n1 >= n3:
    msg = "%d가 가장 큰수" %n1
elif n2 >= n1 and n2 >= n3:
    msg = "%d가 가장 큰수" %n2
else:
    msg = "%d가 가장 큰수" %n3
    
print(msg)