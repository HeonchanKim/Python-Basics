print("한 박스에 라면이 20개 들어갑니다.\n몇 개의 박스가 필요한 지 알려드릴게요")
ramen = int(input("라면 개수 : "))
print("%d박스" %(ramen // 20 if ramen % 20 == 0 else ramen // 20 + 1))
