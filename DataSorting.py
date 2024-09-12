# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 22:56:39 2022

@author: Taijin
"""


import pandas as pd

df = pd.read_excel("D:/PangProjects/SpyderCode/MR/Code/03/50/mrbook.xlsx")

df = df.sort_values(by='销量', ascending=False)
df1 = df.sort_values(by=['图书名称','销量'])

df2 = df.groupby(["类别"])['销量'].sum().reset_index() #按类别分组统计销量并排序
df2 = df2.sort_values(by=['销量'], ascending=False)

df['顺序排名'] = df['销量'].rank(method='first', ascending=False)
print(df[['图书名称','销量','顺序排名']])  #销量相同的按出现顺序排名

df['平均排名'] = df['销量'].rank(ascending=False)
print(df[['图书名称','销量','平均排名']])  #销量相同的按顺序排名的平均值进行平均排名