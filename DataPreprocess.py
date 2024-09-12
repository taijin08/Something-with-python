# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 20:07:24 2022

@author: Taijin
"""


import pandas as pd

pd.set_option('display.unicode.east_asian_width', True) #汉字列输出对齐
df = pd.read_excel('D:/PangProjects/SpyderCode/MR/Code/03/37/TB2018.xls')
print(df)
print(df.info())

print(df.isnull())
print(df.notnull())

df1 = df.dropna()

df2 = df[df['宝贝总数量'].notnull()] #只删除某一中缺失数据

df['宝贝总数量'] = df['宝贝总数量'].fillna(0) #缺失值填充

PD = pd.read_excel('D:/PangProjects/SpyderCode/MR/Code/03/40/1月.xlsx')

print(PD)
print(PD.duplicated())
if True in PD.duplicated():
    PD1 = PD.drop_duplicates(['买家会员名'],keep='last',inplace=False) #删除指定的重复值
    print(PD1)
    
#自动数据对齐
s1 = pd.Series([10,20,30], index=list('abc'))
s2 = pd.Series([2,3,4], index=list('bcd'))
print(s1 + s2)

#重新设置索引
print(s1)
print(s1.reindex(list('abcde'), fill_value=0))

PD2 = PD.set_index(['类别'])  
PD3 = PD.set_index(['类别'], drop=True)  
#为删除后的表重新设置索引
print(df1.reset_index(drop=True))
