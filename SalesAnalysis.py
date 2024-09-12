# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 09:28:52 2022

@author: Taijin
"""

import pandas as pd
import matplotlib as plt

plt.rcParams['font.sans-serif'] = ['SimHei']

data = pd.DataFrame({'Month':['Jan','Feb','Mar','Apr','May','Jun'], 'Sale':[12388, 10090, 8900, 5600, 3200, 20009]})

data.plot.bar(x = 'Month', y = 'Sale', color = ['#9400D3', '#9932CC', '#4B0082', '#8A2BE2', '#9370DB', '#7B68EE'])

print("Analysis Completed!")