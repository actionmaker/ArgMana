#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 14:39:43 2022

@author: actionmaker
"""

import pandas as pd

df = pd.read_csv('/Users/actionmaker/Desktop/Argmana/anagrams.csv',header=None)
df.rename(columns={0: 'w1', 1: 'w2'}, inplace=True)

wset = set(line.strip() for line in open('words_nltk_plus'))

def anagram(row):
    word1_lst = [l for l in row['w1']]
    word2_lst = [i for i in row['w2']]
    return sorted(word1_lst) == sorted(word2_lst)

def healthchecks(df,wset):
    df['w1_in_wordslist'] = df['w1'].apply(lambda x: x in wset)
    df['w2_in_wordslist'] = df['w2'].apply(lambda x: x in wset)
    df['w1_eq_w2'] = df['w1'] == df['w2']
    df['is_anagram'] = df[['w1','w2']].apply(anagram,axis=1)
    

healthchecks(df,wset)
           
df.drop(['w1','w2'],axis=1).value_counts()



