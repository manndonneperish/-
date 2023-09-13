dic_repertory = {'酱油': 50, '醋': 60, '盐': 100, '糖': 120, '鸡精': 20, '麻油': 40}
dic_change = {'酱油': 100, '醋': 80, '鸡精': 50, '蚝油': 60}
dic_repertory.update(dic_change)
lst = [(v, k) for k, v in dic_repertory.items()]
Max = max(lst)
Min = min(lst)
print('{}最多，有{}'.format(Max[1], Max[0]))
print('{}最少，有{}'.format(Min[1], Min[0]))
