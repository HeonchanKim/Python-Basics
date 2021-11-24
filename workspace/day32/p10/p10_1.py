#%% 1번
phone = input("전화번호를 입력하세요 >>>")
# print("국번 : " + phone.split("-")[1])

start = phone.index('-') + 1
end = phone.index('-', start)
code = phone[start:end]
print("국번 : " + code)