#%% list task
# =============================================================================
# 1 ~ 100 까지 값 넣고 출력
# 1 ~ 100 까지 중 짝수만 넣고 출력
# A ~ F 까지 넣고 출력
# A ~ F 까지 중 C 제외하고 출력
# aBcDeGFgHiJkLmNoPqRs...Z 넣고 출력
# "ABC"에서 B를 Z로 변경하기
# 
# 자연수를 한글로 변경하기
# 입력 예)1024
# 출력 예)일공이사
# =============================================================================
# 1 ~ 100 까지 값 넣고 출력
# dataList = []
# for i in range(100):
#     # dataList[i] = i + 1
#     dataList.append(i+1)
    
# print(dataList)

# dataList = [0] * 100
# for i in range(100):
#     dataList[i] = i + 1
    
# print(dataList)
# -----------------------------------------------------------------------
# 1 ~ 100 까지 중 짝수만 넣고 출력
# dataList = [0] * 50

# for i in range(len(dataList)):
#     dataList[i] = (i + 1) * 2
# print(dataList)

# -----------------------------------------------------------------------
# A ~ F 까지 넣고 출력
# dataList = []
# for i in range(6) :
#     dataList.append(chr(i + 65))
    
# print(dataList)
# -----------------------------------------------------------------------
# A ~ F 까지 중 C 제외하고 출력
# dataList = [""] * 5
# 0 A, 1 B, 2 D

# for i in range(len(dataList)):
#     dataList[i] = chr((i + 1 if i > 1 else i) + 65)
    
# print(dataList)

# temp = 0

# for i in range(len(dataList)):
#     temp = i
#     if temp > i:
#         temp += 1
#     dataList[i] = chr(65 + temp)
    
# print(dataList)


# for i in range(len(dataList)):
#     if i > 1:
#         i += 1
#     dataList[i] = chr(65 + i)
    
# print(dataList)

# -----------------------------------------------------------------------
# aBcDeGFgHiJkLmNoPqRs...Z 넣고 출력
# dataList = [""] * 26
# for i in range(len(dataList)):
#     dataList[i] = chr(97 + i if i % 2 == 0 else 65 + i)

# print(dataList)

# for i in dataList:
#     print(i, end="")

# -----------------------------------------------------------------------
# "ABC"에서 B를 Z로 변경하기

# "abcd" : 문자열
# strList = "abcd"
# print(strList[0])
# strList = "ABC"
# strList[1] = "Z"
# print(strList)
# print(strList.replace("B", "Z"))
# strList = strList.replace("B", "Z")
# print(strList)
# -----------------------------------------------------------------------
# 자연수를 한글로 변경하기
# 입력 예)1024
# 출력 예)일공이사

# =============================================================================
# 1) 1024 % 10 == 4
# 2) 1024 // 10 == 102
# 3) 102 % 10 == 2
#     .
#     .
#     .
# =============================================================================

# num = int(input("자연수 입력 : "))
# hangle = "공일이삼사오육칠팔구"
# result = ""

# while num != 0:
#     result = hangle[num % 10] + result
#     num = num // 10

# print(result)






