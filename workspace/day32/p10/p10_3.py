std = '"김철수",85'
name = std.split(",")[0].strip('"')
age = std.split(",")[1]
print("이름은 {}이고, 점수는 {}입니다".format(name,age))