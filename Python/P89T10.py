import pandas as pd
import matplotlib.pyplot as plt
# import numpy as np
import matplotlib

df = pd.read_csv("2018世界杯球队数据.csv", encoding='gb2312')
s1 = df['进球'] - df['失球']
print()

for i in range(len(df['球队'])):
    if s1[i] > 0:
        print(df['球队'][i])
print()

df2 = df[df['红牌'] > 0]
print(df2['球队'])
print()

s2 = df['进球'] / df['射门']
for i in range(len(df['进球'])):
    if s2[i] > 0.1:
        print(df['球队'][i], df['进球'][i], df['射门'][i])
print()

s = sum(df['进球']) / len(df['进球'])
for i in range(len(df['球队'])):
    if df['进球'][i] > s and df['黄牌'][i] < 5:
        print(df['球队'][i], df['进球'][i], df['黄牌'][i])
print()

df = df.sort_values(['进球'], ascending=False)
print(df[['球队', '进球']])
print()

group1 = df.groupby('所属洲')
total = group1.sum()
group1 = total.sort_values(['进球'])
print(group1['进球'])
print()

matplotlib.rcParams['font.family'] = 'SimHei'
plt.ylabel('进球数')
group1['进球'].plot(kind='bar')
plt.show()
