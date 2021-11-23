n = 1
dan = 2
while n <= 9:
    dan = 2
    while dan <= 9:
        print("%d*%d=%d" %(dan, n, dan*n), end='\t')
        dan += 1
    print()
    n += 1