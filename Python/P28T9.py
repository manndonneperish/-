a = input("请输入1~9的一个整数:")
n = int(input("请输入一个正整数:"))
s = 0
for i in range(1, n + 1):
    s += int(str(a) * i)
print("s=", s)
