# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 11:15:13 2022

@author: Taijin
"""


import pandas as pd

data = [[110,105,99],[105,88,115],[109,120,130],[112,115]]
name = ['Jack', 'Tom', 'Tony', 'John']
columns = ['Math', 'Mechanics', 'Physics']

df = pd.DataFrame(data=data, index=name, columns=columns)
df1 = df.loc['Jack']  #抽取一行数据

df2 = df.loc[['Jack','Tony']]  #抽取多行数据
df3 = df.iloc[0:3]
df4 = df.iloc[0:3,[2]]

dfif = df.loc[(df['Mechanics']>105) & (df['Math']>88)]  #按指定条件抽取数据

df['English'] = [88,79,60,50] #插入数据
df.loc[:, 'Biology'] = [78,67,50,75] #通过loc插入数据

Geo = [56,67,58,59]
df.insert(1, 'Geography', Geo) #在指定列之后插入1列

df.loc['Ken'] = [100,120,99,89,65,56] #添加一行

df_append = pd.DataFrame({'Math':[120,117,109],'Geography':[44,57,65],
                          'Mechanics':[82,94,103],'Physics':[77,87,86],
                          'English':[44,78,67],'Biology':[55,65,78]}, 
                         index=['Sarah','Ron','Harry'])

df5 = df.append(df_append)

print(df.columns)
df.rename(columns = {'Math':'Math (Honor)', 'Geography':'Geography (Honor)', 
                     'Mechanics':'Mechanics (Honor)', 'Physics':'Physics (Honor)', 
                     'English':'English (Honor)', 'Biology':'Biology (Honor)'}, 
                      inplace=True) #修改列标题
print(df.columns)  

print(df.index)
df.index = range(1,6) #修改行标题

print(df.loc[1, 'Math (Honor)'])
df.loc[1,'Math (Honor)'] = 90 #修改某数据
print(df.loc[1, 'Math (Honor)'])
df.loc[2,'Math (Honor)'] = 100

print(df.drop([1],inplace=False))
print(df)
print(df.drop(labels='Math (Honor)', axis=1, inplace=False))
print(df.drop(index=df[df['Math (Honor)'].isin([100])].index[:], inplace=False)) #按条件删除数据
#删除所有Math中值为100的行
