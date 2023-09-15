dic = {}
n = int(input("请输入偏移数："))
for i in range(26):
    key = chr(ord('a') + i)
    ch = ord(key) + n
    if ch <= 122:
        valuse = chr(ch)
    else:
        valuse = chr(ch - 122 + 96)
    dic[key] = valuse
s = input("请输入明文：")
for j in s:
    if j in dic.keys():
        print(dic[j], end='')
