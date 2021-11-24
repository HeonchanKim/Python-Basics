comp_num = input("사업자 등록 번호를 입력하세요\n예 123-45-67890\n")

# 첫번째 - 인덱스번호가 3일 때
c1 = comp_num.find("-") == 3
# 두번째 - 인덱스번호가 6일 때
c2 = comp_num.find('-', 4)  == 6
# 총 길이가 12일 
c3 = len(comp_num) == 12
# 각 번호가 전부 숫자인지 검사
c4 = comp_num.replace("-", "").isdecimal()

if c1 and c2 and c3 and c4:
    print("올바른 사업자 등록 번호입니다.")
else:
    print("잘못된 사업자 등록 번호입니다.")


















