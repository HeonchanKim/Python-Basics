#%% method task
# 5개의 정수 중 최대값과 최소값을 구해주는 메소드
def getMaxAndMin(dataList):
    maxData = dataList[0]
    minData = dataList[0]
    resultList = []
    for i in range(1, len(dataList)):
        if maxData < dataList[i]:
            maxData = dataList[i]
        if minData > dataList[i]:
            minData = dataList[i]
    # resultList.append(maxData)
    # resultList.append(minData)
    # return resultList
    return maxData, minData


dataList = [3, 5, 7, 8]
result = getMaxAndMin(dataList)
print(type(result))
print("최대값 : " + str(result[0]))
print("최소값 : " + str(result[1]))

#%% method task2
# 소문자를 대문자로 바꿔주는 메소드
def changeToUpper(string):
    result = ""
    for i in string:
        if ord(i) >= 97 and ord(i) <= 122:
            result += chr(ord(i) - 32)
        else:
            result += i
    return result

print(changeToUpper("AsdfTTTTTtttt123!@#$"))


#%% method task3
# 한글을 정수로 바꿔주는 메소드(일공이사 -> 1024)
def changeToInteger(hangle):
    hangle_org = "공일이삼사오육칠팔구"
    result = ""
    for i in hangle:
        result += str(hangle_org.index(i))
    return int(result)

print(changeToInteger("일공이사") + 1)

#%% 전역변수(global variable)

result = 0

def add(num1, num2 = 0):
    global result
    result = num1 + num2
    # return num1 + num2

def sub(num1, num2):
    global result
    result = num1 - num2
    # return num1 - num2

add(10)
sub(10, 5)
print(result)
# =============================================================================
#                   전역변수              지역변수
# 함수 안에서 읽기    가능                 가능
# 함수 안에서 수정    불가(global)         가능
# 
# 함수 밖에서 읽기    가능                 선언된 지역에서만 가능
# 함수 밖에서 수정    가능                 불가
# =============================================================================








