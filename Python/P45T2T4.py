# 2
dic_student = {}
for i in range(5):
    name = input("请输入学生姓名：")
    age = int(input("请输入学生年龄："))
    dic_student[name] = age
for j in dic_student:
    if len(j) == 3:
        print("{: <5}{}".format(j, dic_student[j]))
    elif len(j) == 2:
        print("{: <6}{}".format(j, dic_student[j]))

# 4
dic_student = {}
for i in range(5):
    name = input("请输入学生姓名：")
    age = int(input("请输入学生年龄："))
    tal = int(input("请输入学生身高（cm）："))
    wei = int(input("请输入学生体重（kg）："))
    lis = [age, tal, wei]
    dic_student[name] = lis
for j in dic_student:
    if len(j) == 3:
        print("{: <5}{}    {}cm    {}kg".format(j, dic_student[j][0], dic_student[j][1], dic_student[j][2]))
    elif len(j) == 2:
        print("{: <6}{}    {}cm    {}kg".format(j, dic_student[j][0], dic_student[j][1], dic_student[j][2]))
