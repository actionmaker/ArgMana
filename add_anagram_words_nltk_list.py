#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 15:31:36 2022

@author: actionmaker
"""

from nltk.corpus import words
import pandas as pd

df = pd.read_csv('/Users/actionmaker/Desktop/Argmana/anagrams.csv',header=None)
df.rename(columns={0: 'w1', 1: 'w2'}, inplace=True)
wset_nltk = list(words.words())

df['w1_in_nltk'] = df['w1'].apply(lambda x: x in wset_nltk)
df['w2_in_nltk'] = df['w2'].apply(lambda x: x in wset_nltk)
#set(df['w1'][(df['w1_in_nltk']==False)])

wset_nltk_plus = set(wset_nltk).union(set(df['w1'])).union(set(df['w2']))
df['w1_in_nltk_plus'] = df['w1'].apply(lambda x: x in wset_nltk_plus)
df['w2_in_nltk_plus'] = df['w2'].apply(lambda x: x in wset_nltk_plus)

df[['w1_in_nltk_plus','w2_in_nltk_plus']].value_counts()


textfile = open("words_nltk_plus", "w")
for element in wset_nltk_plus:
    textfile.write(element + "\n")
textfile.close()
