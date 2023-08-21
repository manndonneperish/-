kindman = ["甲", "乙", "丙", "丁"]
for x in kindman:
    if (x != "甲") + (x == "丙") + (x == "丁") + (x != "丁") == 3:
        print("做好事的人是：", x)
        break
