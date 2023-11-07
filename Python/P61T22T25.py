# 22
def isdiff(n):
    s = str(n)
    m = set(s)
    if len(s) == len(m):
        return True
    else:
        return False

low = int(input('请输入最小值：'))
high = int(input('请输入最大值：'))
count = 0
print('{: <8}{}'.format('x', 'x*x'))
for i in range(low, high + 1):
    if isdiff(i * i):
        print('{}\t{}'.format(i, i * i))
        count += 1
print('总数为{}'.format(count))

# 25
f = lambda x: x * x
ls = eval(input('请输入一个列表：'))
s = 0
for i in ls:
    s += f(i)
print(s)
