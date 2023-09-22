# 6
def isLeap(n):
    if (n % 4 == 0 and n % 100 != 0) or n % 400 == 0:
        return True
    else:
        return False


count = 0
for i in range(1900, 2021):
    if isLeap(i):
        print(i, end=' ')
        count += 1
        if count % 5 == 0:
            print()


# 11
def f(a, n):
    s = 0
    for i in range(1, n + 1):
        b = int(str(a) * i)
        s += b
    return s


a = int(input('请输入一个整数(1-9)：'))
n = int(input('请输入一个正整数：'))
print(f(a, n))
