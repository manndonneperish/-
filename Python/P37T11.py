lst_info = [["李玉", "男", 25], ["金忠", "男", 23], ["刘妍", "女", 21], ["莫心", "女", 24], ["沈冲", "男", 28]]
i = input("请输入要删除的员工姓名：")
while i != "0":
    for info in lst_info:
        if info[0] == i:
            lst_info.remove(info)
            print(lst_info)
            break
        else:
            print("该员工不存在")
    i = input("请输入要删除的员工姓名：")
print("程序结束")
