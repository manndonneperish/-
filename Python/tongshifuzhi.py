a, b = map(int, input().split(","))  # 同时给a,b赋值为从键盘接收的整数，split的作用为分隔，分隔符为（,），此时输入格式为(2,5)
s = 0
for i in range(a, b + 1):
    s += i
print(s)
