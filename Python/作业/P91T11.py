# encoding:utf-8

import pandas as pd
import matplotlib.pyplot as plt
# import numpy as np
import matplotlib
import os

os.chdir('作业/')

df = pd.read_excel('score.xls')
df['总分'] = df[['高数', '英语', '政治', '体育']].sum(axis=1)
df['均分'] = df['总分'] / 4
print(df)
df.to_csv('score.csv')
df1 = df[df['均分'] > 85]
print(df1[['班级', '姓名']])
print()

s = df['高数'].sum()
df2 = df[df['高数'] > s / len(df['姓名'])]
print(df2[['班级', '姓名']])
print()

df = df.sort_values(['总分'], ascending=False)
print(df)
print()

matplotlib.rcParams['font.family'] = 'SimHei'
plt.xlabel('学科')
plt.ylabel('成绩')
plt.title('五门课程成绩箱型图')
