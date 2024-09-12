# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 10:06:35 2022

@author: Taijin
"""

import pandas as pd

df = pd.read_excel('data.xlsx')
df1 = df.head()
df2 = pd.read_excel('data.xlsx', index_col=0)
df3 = pd.read_excel('data.xlsx', usecols=[1,3])

s1 = pd.Series([88, 60, 75], index=['Jack','Tom','Tony'])
print(s1)
print(s1[0])
print(s1['Jack':'Tony'])

data = [[110,105,99], [105,88,115], [109,120,130]]
index = [0,1,2]
columns = ['Math', 'Physics', 'Chemistry']
DF = pd.DataFrame(data = data, index = index, columns = columns)
print(DF)
print('-'*20)
for col in columns:
    s = DF[col]
    print(s)
    
df4 = pd.read_csv('1月.txt', sep='\t', encoding='ansi')


    
