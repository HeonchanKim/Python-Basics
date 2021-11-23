while True:
    star = int(input("이번 영화의 평점을 입력하세요 >>> "))
    if star >= 1 and star <= 5:
        print("평점 : {}".format('★' * star))
        break
    else:
        print("1~5까지만 입력하세요")