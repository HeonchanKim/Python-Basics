class Quiz:
    answer = ['경기도', '강원도', '충청남도', '충청북도', '전라남도', '전라북도', '경상남도', '경상북도', '제주특별자치도']
    
    @classmethod
    def chanllenge(cls):
        if not cls.answer:
            print("모두 맞췄습니다. 성공!")
            return
        do = input("정답은? >>> ")
        if do not in cls.answer:
            raise Exception("틀렸습니다.")
        for i, answer_do in enumerate(cls.answer):
            if do == answer_do:
                print("정답입니다.")
                cls.answer.pop(i)
                cls.chanllenge()
        

try:
    print("우리나라 9개 도를 맞히는 퀴즈입니다. 하나씩 입력하세요")
    Quiz.chanllenge()
except Exception as e:
    print(e)
    
    
    
    
    
    
    
    
    