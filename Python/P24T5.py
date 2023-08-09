y = eval(input('请输入一个年份'))
if y % 400 == 0 or (y % 4 == 0 and y % 100 != 0):
    print('该年为闰年')
else:
    print('该年不为闰年')
