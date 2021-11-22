emp_no = int(input("4자리 사원번호를 입력하세요>>>"))
emp_last_no = emp_no % 10
print("근무 시간은 %s입니다."%('오전' if emp_last_no >= 5 else '오후'))
