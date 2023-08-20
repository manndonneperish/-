busstop = ["龙江新城市", "阳光广场", "汉江路", "嫩江路", "清凉山公园", "拉萨路", "五台山", "莫愁路"]
x = input("请输入起始站：")
y = input("请输入终点站：")
i = busstop.index(x)
j = busstop.index(y)
if i == j:
    print("请重新输入")
elif i < j:
    k = j - i
    print("从{}站前往{}站需要{}站路".format(x, y, k))
else:
    print("您需要乘坐反方向线路")
