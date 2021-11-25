fileName = ""

while True:
    fileName = input("복사할 파일명을 입력하세요 >>>")
    extName = fileName[fileName.rfind(".") + 1:]
    
    if extName != "txt":
        print("복사할 수 없는 파일입니다.")
    else:
        break

with open(fileName, 'rt', encoding='utf-8') as source:
    with open("복사본-" + fileName, 'wt') as copy:
        while True:
            buffer = source.read(1)
            if not buffer:
                break
            copy.write(buffer)
print("복사본-"+fileName+"파일이 생성되었습니다.")







