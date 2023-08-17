import random

RND1 = random.randint(0, 100)
RND2 = random.randint(0, 100)
print("RND1=", RND1)
print("RND2=", RND2)
for i in range(min(RND1, RND2), 0, -1):
    if RND1 % i == 0 and RND2 % i == 0:
        print("最大公约数为:", i)
        x = i
        break
n = RND1 * RND2 / x
print("最小公倍数为:", n)
