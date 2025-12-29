# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 14:33:36 2024

@author: yyyyyyyyyyyyyyyyyyyy
"""

def fix_spelling_correct_words_in_web(self):
     """ fix all spelling all words in web so they properly connect """
     # find previous code on this
     # what are alternative approaches to this
     # use this for both of the above functions
     # add in a spelling component to make it easier to find previous objects
     # and remove extra spacing arund words in web
     import re
     from nltk.tokenize import word_tokenize
     from spellchecker import SpellChecker
     spell = SpellChecker()
     counterr=0
     fixed_word_list=[]
     final_para_list=[]
     
     with open (input_file,"r") as f:
         text=str(f.read())    
     paragraph_list=text.split("\n")
     for i, paragraph in enumerate(paragraph_list):
         if paragraph=="":
             continue
         word_list=word_tokenize(paragraph)
         fixed_word_list=[]
         for word in word_list:
             word_fixed=re.sub("[^A-Za-z\.]","", word)
             if word_fixed =="":
                 continue
             fixed_word = spell.correction(word_fixed)
             if fixed_word==None:
                 continue
             fixed_word_list.append(fixed_word)
         if fixed_word_list:
             text_from_doc=" ".join(fixed_word_list)
             final_para_list.append(text_from_doc)
     return final_para_list