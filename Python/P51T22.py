set_highjump = {"李朋", "王宇", "张锁", "刘松山", "白旭", "李晓亮"}
set_longjump = {"王宇", "唐英", "刘松山", "白旭", "刘小雨", "宁成"}
print("参加比赛的所有学生为：", set_highjump | set_longjump)
print("两项比赛都参加的学生为：", set_highjump & set_longjump)
print("仅参加了跳高的学生为：", set_highjump - set_longjump)
print("仅参加了跳远的学生为：", set_longjump - set_highjump)
print("仅参加了一项比赛的学生为：", set_longjump ^ set_highjump)
