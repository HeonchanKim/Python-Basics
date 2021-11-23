for dan in range(2, 10):
    if dan % 2 == 0:
        print()
        continue
    for i in range(1, dan+1):
        print("{}*{}={}".format(dan, i, dan*i))