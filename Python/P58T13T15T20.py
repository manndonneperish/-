# 13
def isdiff(n):
    s = str(n)
    for i in s:
        if s.count(i) > 1:
            return 0
        break
    else:
        return 1


n = int(input('请输入一个正整数：'))
print(isdiff(n))


# 15
def f(ls):
    a = set(ls)
    if len(a) < len(ls):
        return True


ls = eval(input('请输入一个列表：'))
print(f(ls))


# 20
def delSame(li):
    t = []
    for i in li:
        if i not in t:
            t.append(i)
    return t


li = eval(input('请输入一个列表：'))
print(delSame(li))
