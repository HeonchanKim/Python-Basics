def vending_machine(money):
    price = 700
    count = money // 700
    change = 0
    for i in range(count):
        change = money - (i + 1) * price
        print("음료수는 = %d개, 잔돈 = %d원" %(i+1, change))
        
vending_machine(3000)