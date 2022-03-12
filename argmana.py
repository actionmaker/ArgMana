#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
wset = set(line.strip() for line in open('words_nltk_plus'))

with open('anagrams.csv') as f:
    lines = f.readlines()
    ana1,ana2 = random.choice(lines).strip().split(',')

cond1 = False
cond2 = False


tries = 0
first = True
cond = cond1 & cond2
history = []
print("Welcome to Argmana!")
print("Your goal is to find two secret anagrams. Enter words and gather clues.") 
print("If you want to give up then just enter 'quit'.")
print("Good Luck!")
clues = set()

while(not cond):
    word = input('Input a word, any word: ').lower()
    if(word not in wset):
        print("That's not a word afaik...")
        tries = tries + 1
        history.append(word)
        print("Score: ", tries)
        print("History: ", history)
        if clues == set(ana1):
            print('You found all the letters in the anagrams: ',','.join(clues))
        else:
            print('Letters discovered in the anagrams: ',','.join(clues))
    else:
        history.append(word)
        tries = tries + 1
        jumble = set(word).intersection(ana1)
        if first:
            clues = jumble
            first = False
        else:
            clues = clues.union(jumble)
        print("Score: ", tries)
        print("History: ", history)    
        if clues == set(ana1):
            print('You found all the letters in the anagrams: ',','.join(clues))
        else:
            print('Letters discovered in the anagrams: ',','.join(clues))
        if word == ana1:
            cond1 = True
        if word == ana2:
            cond2 = True
        cond = cond1 & cond2
        if cond1:
            print("You found the first word: "+ana1)
        if cond2:
            print("You found the second word: "+ana2)
        if word == 'quit':
            cond = True
    print("\n")
        

if word == 'quit':
    print("\n"*5)
    print("__________________________________________")
    print("Quitter")
    print("The anagrams were: "+ana1+", "+ana2)
    print("__________________________________________")
else:
    print("\n"*5)
    print("__________________________________________")
    print("WINNER! WINNER! WINNER!")
    print("The anagrams were: "+ana1+", "+ana2)
    print("You figured it out in ",tries," attempts!")    
    print("__________________________________________")
