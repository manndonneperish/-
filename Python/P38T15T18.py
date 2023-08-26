# 15
i = input("请输入一串英文：")
lst = i.split(" ")
print(" ".join(lst[-1::-1]))

# 18
j = "语文:80,数学:82,英语:90,物理:85,化学:88,美术:80"
lst = j.split(",")
s = [int(x[3:5]) for x in lst]
z = sum(s)
avg = z / len(s)
print("总分为：{}，平均分为：{:.1f}".format(z, avg))
