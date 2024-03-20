# encoding:utf-8

import pandas as pd
import os

os.chdir('作业/')

import numpy as np
df = pd.read_csv('tourist_statistic.csv')
df['平均入境游客(万人次)']=df.mean(axis=1).round(4)
df.to_csv('tourist_statistic.csv')
df3 = df[(df['所属洲'] == '亚洲') & (df['2018年'] > 180)]
print(df3['指标(万人次)'].str[:-4])
df4=df[(df['所属洲']=='欧洲')&(df['指标(万人次)']=='俄罗斯入境游客')]
print((df4['2018年']-df4['2009年'])/df4['2009年'])
df5=df.loc[:,'2009年':'2018年'].sum()
print(df5)
group=df.groupby('所属洲')
print(group)
group1=group[['所属洲','2010年','2014年','2018年']]
total=group1.sum()
print(total)
df6=pd.DataFrame(total)
group2=df6.sort_values(['2018年'],ascending=False)
print(group2)
