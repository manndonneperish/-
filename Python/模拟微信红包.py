import random

money = eval(input('请输入红包总金额：'))
person = eval(input('请输入红包个数：'))
M = money
lst = []
for N in range(person, 1, -1):
    lucky = random.uniform(0.01, 2 * M / N)
    lucky = round(lucky, 2)
    lst.append(lucky)
    M -= lucky
lst.append(round(M, 2))
print(lst)
print(abs(sum(lst) - money) <= 1e-5)
