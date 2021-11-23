for n in range(1, 100):
    units = n % 10
    tens = n // 10
    
    c1 = units % 3 == 0 and units != 0
    c2 = tens % 3 == 0 and tens != 0
    
    if c1 and c2:
        print("짝짝", end='\t')
    elif c1 or c2:
        print("짝", end='\t')
    else:
        print(n, end='\t')
        
    if n % 10 == 0:
        print()
    