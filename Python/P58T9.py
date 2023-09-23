def f(n):
    s = 0
    for i in range(1, n):
        if n % i == 0:
            s += i
    if s == n:
        return 1
    else:
        return 0


n = int(input('请输入一个自然数：'))
print(f(n))
