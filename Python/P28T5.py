n = 20
x1 = x2 = 1
count = 2
print("{:>8}{:>8}".format(x1, x2), end=" ")
for i in range(3, 21):
    x3 = x1 + x2
    print("{:>8}".format(x3), end=" ")
    count += 1
    if count % 5 == 0: print()
    x1, x2 = x2, x3
