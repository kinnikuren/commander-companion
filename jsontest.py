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

def save_df_to_pickle(df, filename):
    df.to_pickle(filename)


def read_df_from_pickle(filename):
    return pd.read_pickle(filename)
    
#write_to_csv(mtg_dict)
            
def initialize():
    mtg_dict = read_json_to_dict()

    df = convert_jsondict_to_dataframe(mtg_dict)

    save_df_to_pickle(df,'mtg_pickle.pkl')

def create_commander_pickle():
    df = read_df_from_pickle('mtg_pickle.pkl')
    df_commander = df[df['legalities.commander'] == 'Legal'].reset_index()
    print(len(df_commander))
    
    save_df_to_pickle(df_commander, 'mtg_cmdr_pickle.pkl')

#initialize()
#create_commander_pickle()

df = read_df_from_pickle('mtg_cmdr_pickle.pkl')

print(df.head())
print(len(df))
#print(df['legalities.commander'])

#df_legendary_creatures = df[df['types']
#print(df['Creature' in df['types']])
df_commanders = df[(df['types'].map(lambda x: 'Creature' in x)) & (df['supertypes'].map(lambda x: 'Legendary' in x))]
print(df_commanders)
print(len(df_commanders))
#print(df[(df['supertypes'].map(lambda x: 'Legendary' in x))])

pd_test = pd.DataFrame()

count = 0
for index, row in df.iterrows():
    if 'Creature' in row['types']:
        #pd_test.append(row)
        count+=1
    try:
        if type(row['types']) != list:
            print('hello')
        if len(row['types']) == 0:    
            print('hey')
    except TypeError:
        print(row['name'])
print(count)
print(type(df['types']))
print(df.iloc[0]['types'])

#print(df[df['types'].isin(['Creature'])])

#print(df['types'])

#print(df['types'].unique)


#print(df[df.name == 'Counterspell'])



#df_cmc = df.groupby('convertedManaCost').name.count().reset_index()
#print(df_cmc)

def bar_plot(x, y):
    plt.bar(x, y)
    plt.xlim([0,16])
    plt.show()



