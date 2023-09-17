def isOdd(n):
    if n % 2 == 0:
        return True
    else:
        return False


n = int(input('请输入一个整数：'))
print(isOdd(n))
