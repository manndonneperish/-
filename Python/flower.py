i = eval(input("请输入一个三位数："))
a, j = divmod(i, 100)
b, j = divmod(j, 10)
c = j
if a ** 3 + b ** 3 + c ** 3 == i:
    print("It's a flower")
else:
    print("It's not a flower")
