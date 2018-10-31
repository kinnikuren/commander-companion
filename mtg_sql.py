# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 21:34:18 2018

@author: alanyliu
"""

import sqlite3
import json

conn = sqlite3.connect('mtg_sql.db')

c = conn.cursor()

def create_table():
    # Create table
    c.execute('''CREATE TABLE mtg_cards
                 (name text)''')

mtg_dict = {}

with open('mtgjson/AllCards.json', 'r',encoding='utf-8') as myfile:
    #data = myfile.read()
    mtg_dict = json.load(myfile)

# Insert a row of data
for key in mtg_dict:
    t = (key,)
    #print(t)
    c.execute("INSERT INTO mtg_cards VALUES (?)", t)

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()
