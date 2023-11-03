def judge(password):
    level = 0
    n = len(password)
    if n >= 8:
        level += 1
    for ch in password:
        if '0' <= ch <= '9':
            level += 1
            break
    for ch in password:
        if 'A' <= ch <= 'Z':
            level += 1
            break
    for ch in password:
        if 'a' <= ch <= 'z':
            level += 1
            break
    return level


while True:
    password = input('请输入测试密码（直接按回车退出）：')
    if password == '':
        break
    level = judge(password)
    print('{}的密码强度为{}级'.format(password, level))
