lst_staff = ["李梅", "张富", "付妍", "赵诺", "刘江"]
dic_award = {"张富": 10000, "赵诺": 15000}
for i in lst_staff:
    if i in dic_award:
        print("{}的年终奖金额为{}元".format(i, dic_award[i]))
    else:
        print("{}的年终奖金额为5000元".format(i))
