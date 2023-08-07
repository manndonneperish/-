# 1
n = int(input("请输入一个整数:"))
if n % 3 == 0 and n % 7 == 0:
    print("YES")
else:
    print("NO")

# 3
ch = input("请输入一个字符：")
if ch.isdigit():
    print('输入的是数字')
elif ch.isalpha():
    print('输入的是字母')
else:
    print('输入的是其他字符')
