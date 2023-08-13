# 3
for i in range(1, 101):
    if i % 3 == 0 and i % 5 != 0:
        print(i, end=" ")

# 4
k = 1
for y in range(1000, 2001):
    if (y % 100 != 0 and y % 4 == 0) or (y % 400 == 0):
        print(y, end=" ")
        k += 1
        if k % 5 == 0: print()
