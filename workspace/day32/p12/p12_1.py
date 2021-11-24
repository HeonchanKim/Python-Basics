# =============================================================================
# 모듈 : .py파일
# 패키지 : 모듈을 담고 있는 폴더
# 계산기 폴더 안에 사칙연산 파이썬 파일 4개가 있다면,
# 계산기 패키지 안에, 모듈이 4개 있는 것이다.
# =============================================================================

# =============================================================================
# import 모듈명
# from 모듈 import 함수
# from 모듈 import 함수1, 함수2
# from 모듈 import 함수 *
# =============================================================================

import random
import time

pot = [n for n in range(1, 46)]
jackpot = []
for n in range(1, 7):
    random.shuffle(pot)
    pick = pot.pop()
    print("{}번째 당첨번호는 {}입니다.".format(n, pick))
    jackpot.append(pick)
    time.sleep(2)

jackpot.sort()
print("이번 당첨 번호는 {} 입니다.".format(jackpot))
