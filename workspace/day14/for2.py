# =============================================================================
# A~F까지 출력
# A~F까지 중 C제외하고 출력
# aBcDeFgHiJkLmNoPqRsTuVwXyZ 출력
# =============================================================================
# 1번 문제
# A B C D E F
# print(ord('A'))
# print(ord('B'))
# range(start, end, step)
# start가 0일 때에는 생략이 가능하다.
# step이 1일 때에는 생략이 가능하다.
# for i in range(0, 6, 1)
# for i in range(6):
#     print(chr(i + 65))

# 2번 문제
# A~F까지 중 C제외하고 출력
# for i in range(5):
#     # 0 1 2 3 4
#     # A B C D E
#     if i > 1:
#         i += 1
#     print(chr(65 + i))

# temp = 0
# for i in range(5):
#     # i값을 직접 변경하고 싶지 않기 때문에
#     # temp라는 변수에 담고 temp를 변경한다.
#     # temp는 저장공간이고, i는 값이다.
#     temp = i
#     temp = temp + 1 if i > 1 else temp;
#     print(chr(65 + temp))

# 3번 문제
# aBcDeFgHiJkLmNoPqRsTuVwXyZ 출력
# 97 66 99 68 101 70
# for i in range(26):
#     # ??? % 2 == 0 짝수
#     # ??? % 2 != 1 홀수
    
#     print(chr(97 + i) if i % 2 == 0 else chr(65 + i), end="")

