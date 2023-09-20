# 7
def f(n):
    s = str(n)
    ls = [int(i) for i in s]
    Sum = sum(ls)
    return Sum


n = int(input('请输入一个正整数：'))
print(f(n))


# 8
def f(n):
    s = str(n)
    ls = [int(i) for i in s]
    Sum = sum(ls)
    return Sum


a = 0
for n in range(100, 1000):
    if f(n * 3) == f(n * 4) == f(n * 5) == f(n * 6) == f(n * 7):
        print('x={}:x*3={},x*4={},x*5={},x*6={},x*7={}'.format(n, n * 3, n * 4, n * 5, n * 6, n * 7))
        a += 1
print('共有{}个符合条件的三位数。'.format(a))
