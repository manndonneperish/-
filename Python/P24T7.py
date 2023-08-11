import math

a = float(input("请输入三角形边长a:"))
b = float(input("请输入三角形边长b:"))
c = float(input("请输入三角形边长c:"))
if a + b > c and a + c > b and b + c > a:
    h = (a + b + c) / 2
    S = math.sqrt(h * (h - a) * (h - b) * (h - c))
    print("三角形的面积为：{:.2f}".format(S))
else:
    print("输入的三边无法构成三角形")
