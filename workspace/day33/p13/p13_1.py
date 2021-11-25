nation = ['그리스', '아테네', '독일', '베를린', '러시아', '모스크바', '미국', '워싱턴']
file = open('nation.txt', "wt")

for idx, country in enumerate(nation):
    if idx % 2 == 0:
        file.write(nation[idx] + "-" + nation[idx+1] + "\n")
file.close()

