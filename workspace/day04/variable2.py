#%% (1) test1

print("이름 : ", end='')
print(name)
print("나이 : ", end='') 
print(age, end='살\n')
# print("살\n")
print("키 : ", end='')
print(height, end='cm\n')
print("취미 : ", end='')
print(hobby)

#%% (2) test2
# 서식문자(format)
# 반드시 따옴표 안에서 작성한다.
# %d : decimal 정수(10진수)
# %o : octal 정수(8진수)
# %x : hexadecimal 정수(16진수)
# %f : float 실수
# %c : character 문자
# %s : string 문자열
name = "김헌찬"
age = 26
height = 170.999
hobby = "영화"

print("이름 : %s" %name)
print("나이 : %d" %age)
print("키 : %.2fcm" %height)
print("취미 : %s" %hobby)
