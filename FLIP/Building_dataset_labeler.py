# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 23:57:15 2023

@author: rossg
"""
import re
import numpy as np
import nltk 

from nltk.tokenize import sent_tokenize

from nltk.tokenize import word_tokenize
print( "Is there a value in the sentence you need to assign here 1 for yes or any other value to answer no")
sentence = "the dog walked   hello   to the park and   took  a shit."

has_useful_value = int(input())

if has_useful_value == 1:
    
    

    zero_list= [0 for i in range(len(sentence3))]
    stopper= 0
    print("""legislation = 1
    jurisprudence = 2
    articles = 3
    coresponding_page_num = 4
    references_leg = 5
    references_juris = 6
    references_article= 7""")
    print(sentence3)
    
    while stopper != "y": 
        print("Select a word in the sentence to assign a value to.")
        select_word_in_sentence = int(input())
        print(sentence3[select_word_in_sentence])
        print("Now assign a value to this word.")
        starting_point=zero_list[select_word_in_sentence]= int(input())
        print(" Type y to quit. Type n to continue on the same segment. Type s to go back to the sentence level.")
        stopper = input()
        if stopper == "n":
            for i, infinity in enumerate(sentence):
                next_word_value=i+1
                next_word_value=starting_point + next_word_value
                print(sentence3[next_word_value])
                zero_list[next_word_value]=int(input())  
        if stopper == "s":
            continue     
    
        
    
    
    
    