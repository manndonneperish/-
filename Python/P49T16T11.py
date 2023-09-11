# 16
dic_score = {"李刚": 93, "陈静": 78, "张金柱": 88, "赵启山": 91, "李鑫": 65, "黄宁": 83}
lis = [(i, j) for j, i in dic_score.items()]
lis.sort(reverse=True)
Lis = [k[1] for k in lis]
print(Lis)

# 11
dic_score = {"徐丽": [88, 90, 98, 95], "张兴": [85, 92, 95, 98], "刘宁": [89, 89, 90, 92], "张旭": [82, 86, 89, 90]}
for i in dic_score:
    j = dic_score[i]
    k = sum(j) / len(j)
    dic_score[i] = k
print(dic_score)
