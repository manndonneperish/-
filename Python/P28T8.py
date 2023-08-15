ans = 0
for i in range(1, 100, 2):
    for j in range(2, 101, 2):
        for k in range(3, 100, 2):
            pro = i * j * k
            ans += pro
print(ans)
