import matplotlib.pyplot as plt

# 13
dic = {}
s = input('请输入一串英文：')
s.lower()
for i in s:
    if i.isalpha():
        dic[i] = dic.get(i, 0) + 1
print(dic)
x = [j for j in dic]
y = [k for k in dic.values()]
plt.bar(x, y)
plt.show()

# 14
dic = {}
s = 'When in the course of human events, it becomes necessary for one people todissolve the political bands which ' \
    'have connected them with another, and to assume among the powers of the earth, the separate and equal station to ' \
    'which the laws Nature and Nature’s God entitle them, a decent respect to the opinions of mankind requires that ' \
    'they should declare the causes which impelthem to the separation. '
s.replace('，', ' ')
s.lower()
for i in s:
    if i.isalpha():
        dic[i] = dic.get(i, 0) + 1
print(dic)
lst = [(v, k) for k, v in dic.items()]
lst.sort()
print('次数最多的5个单词为：', end='')
for j in range(5):
    print(lst[j][1], end=" ")
x = [a for a in dic]
y = [b for b in dic.values()]
plt.bar(x, y)
plt.show()
