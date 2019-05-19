# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 12:55:49 2018

@author: alanyliu
"""
import pandas as pd

df_commanders = pd.read_pickle('commanders.pkl')

print(df_commanders.head())
print(df_commanders.info())

#print(df_commanders.iloc[0].index)
#print(df_commanders.iloc[0].name)
print(df_commanders.iloc[0])
#print(df_commanders.iloc[0]['level_0'])
print(df_commanders.iloc[0]['name'])
print(df_commanders.iloc[0]['manaCost'])
print(df_commanders.iloc[0]['convertedManaCost'])
print(df_commanders.iloc[0]['type'])
print(df_commanders.iloc[0]['text'])
print(df_commanders.iloc[0]['power'])
print(df_commanders.iloc[0]['toughness'])






