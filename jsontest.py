# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 20:40:43 2018

@author: alanyliu
"""
import json
import csv
import pandas as pd
from pandas.io.json import json_normalize
from matplotlib import pyplot as plt


def read_json_to_dict():
    mtg_dict = {}
    
    with open('mtgjson/AllCards.json', 'r',encoding='utf-8') as myfile:
        #data = myfile.read()
        mtg_dict = json.load(myfile)
        #print(type(json.load(myfile)))
    
    #print(mtg_dict[0])
    #18 fields
    print(len(mtg_dict['1996 World Champion']))
    print(mtg_dict['Abbey Griffin'])
    #print(json.load(data))
    
    return mtg_dict

"""
count = 0
with open ('mtg.csv', "w", newline='') as f:
    writer = csv.writer(f)
    for key in mtg_dict:
        writer.writerow([key])
        #print(key)
"""
"""
        count += 1
        if count > 10:
            break"""
            
def write_to_csv(mtg_dict):
    #fieldnames = list(range(19))
    fieldnames = ['name', 'subtypes', 'supertypes', 'layout', 'type', 'manaCost', 'isReserved', 'colors', 'text', 'types', 'uuid', 'legalities', 'convertedManaCost', 'colorIdentity', 'rulings', 'printings', 'foreignData', 'starter', 'toughness', 'power', 'names', 'loyalty', 'colorIndicator']
    with open('mtg_1.csv', 'w', newline='',encoding='utf-8') as csvfile:
        #fieldnames = ['first_name', 'last_name']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
        writer.writeheader()
        for key, values in mtg_dict.items():
            writer.writerow(values)
            #print(key)

def convert_jsondict_to_dataframe(mtg_dict):
                
    values_list = []
    for key, values in mtg_dict.items():
        values_list.append(values)    
    
    #pd.set_option('display.height', 1000)
    
    pd.set_option('display.max_rows', 500)
    pd.set_option('display.max_columns', 500)
    #pd.set_option('display.width', 500)
    
    
    df = pd.DataFrame.from_dict(json_normalize(values_list), orient='columns')
    
    return df

def save_df_to_pickle(df):
    df.to_pickle('mtg_pickle.pkl')


def read_df_from_pickle():
    return pd.read_pickle('mtg_pickle.pkl')
    
#write_to_csv(mtg_dict)
            
mtg_dict = read_json_to_dict()

df = convert_jsondict_to_dataframe(mtg_dict)

save_df_to_pickle(df)

df = read_df_from_pickle()

#print(df.head())
print(len(df))
print(df[df.name == 'Counterspell'])

df_cmc = df.groupby('convertedManaCost').name.count().reset_index()
print(df_cmc)

plt.bar(df_cmc.convertedManaCost, df_cmc.name)
plt.xlim([0,16])
plt.show()



