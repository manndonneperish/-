# 0漂移
lst = eval(input("请输入数值列表："))
n = lst.count(0)
for i in range(n):
    lst.remove(0)
lst = lst + [0] * n
print(lst)
