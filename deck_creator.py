# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 13:38:52 2018

@author: alanyliu
"""
import pandas as pd
from matplotlib import pyplot as plt
import random

df_commanders = pd.read_pickle('commanders.pkl')
df_commander_cards = pd.read_pickle('mtg_cmdr_pickle.pkl')
total_commander_cards = len(df_commander_cards.index)
total_generals = len(df_commanders.index)

class Deck:
    def __init__(self):
        self.df_deck = pd.DataFrame(columns=df_commander_cards.columns)

    def add_card(self, index):
        self.df_deck.loc[len(self.df_deck.index)] = df_commanders.iloc[index]
    
    def remove_card(self, deck_index):
        print('removing card at index {}'.format(deck_index))
        self.df_deck.drop(index=deck_index,inplace=True)
        self.df_deck.reset_index(drop=True,inplace=True)
        
    def display_deck(self):
        print(self.df_deck['name'])
        #print(self.df_deck)
        
    def display_mana_curve(self):
        print("displaying mana curve...")
        df_manacurve = self.df_deck.groupby('convertedManaCost').name.count().reset_index()
        print(df_manacurve)
        
        plt.bar(df_manacurve['convertedManaCost'],df_manacurve['name'])
        ax = plt.subplot()
        ax.set_xticks(range(0,int(max(df_manacurve['convertedManaCost']))+1))
        plt.show()
        
    def add_random(self):
        for i in range(100):
            self.add_card(random.randint(0,total_generals))

def filter_by_color(color):
    print(len(df_commander_cards.index))
    test = df_commander_cards[df_commander_cards['colorIdentity'].map(lambda x: color in x)]
    print(len(df_commander_cards.index))
    print(len(test.index))


def input_analyzer(user_input, user_deck):
    #print(df_commanders.iloc[0])
    #test_deck = user_deck.df_deck.append(df_commanders.iloc[0])
    
    #print(test_deck)
    
    deck_index = 0
    
    user_inputs = user_input.split(' ')
    
    if user_inputs[0] == 'a':
        if (len(user_inputs) > 1):
            user_deck.add_card(int(user_inputs[1]))
        else:
            print("Please specify card number.")
    elif user_inputs[0] == 'r':
        user_deck.remove_card(deck_index)
    elif user_inputs[0] == 'mc':
        user_deck.display_mana_curve()
    
    print("Number of cards:")
    print(len(user_deck.df_deck))
    
    user_deck.display_deck()


def deck_creator():
    user_deck = Deck()
    
    #user_deck.add_random()
    
    for index, row in df_commanders.iterrows():
        print("{}. {}".format(index,row['name']))
    
    #sel = input("Choose commander:")
    
    #temporary to skip input
    sel = 796
    
    selected_commander = df_commanders.iloc[int(sel)]
    print("selected {}".format(selected_commander['name']))
    print(selected_commander['colors'])
    
    print(df_commander_cards[df_commander_cards['name'] == "Urborg, Tomb of Yawgmoth"].iloc[0]['colorIndicator'])
    
    
    #colorIdentity
    user_input = ''
    while (user_input not in ['exit','x']):
        user_input = input(':')
        input_analyzer(user_input, user_deck)

#deck_creator()
filter_by_color('R')