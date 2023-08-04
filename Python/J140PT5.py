def f1(v):
    if v[0] >= 85 and v[1] >= 85 and v[2] >= 85:
        return True


def f2(n):
    return sum(n) / len(n), sum(n)


def f3(dic):
    ls = [(sum(v), k) for k, v in dic.items()]
    ls.sort()
    Ls = [j[1] for j in ls]
    return Ls


dic = {'01': [67, 88, 45], '02': [97, 68, 85], '03': [97, 98, 95], '04': [67, 48, 45], '05': [82, 58, 75],
       '06': [96, 49, 65]}
print('每门成绩均大于85的学生', end=':')
for k, v in dic.items():
    if f1(v):
        print(k)
for i in dic:
    print('{}的平均分为{:.2f}，总分为{:.2f}'.format(i, f2(dic[i])[0], f2(dic[i])[1]))
print(f3(dic))
