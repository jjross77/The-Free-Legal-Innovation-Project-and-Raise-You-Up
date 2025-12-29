# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 20:15:06 2023

@author: yyyyyyyyyyyyyyyyyyyy
"""

import os
import pickle
with open(r'C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\dicttt_of_sentence_embeddings.pickle', 'rb') as f:
     sentence_list4 = pickle.load(f)
     print(len(sentence_list4))
     #for key, values in sentence_list4.items():
         #print(f"This sentence is {key}")
        
with open(r'C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\dict_2_of_embeddings.pickle', 'rb') as ff:
     sentence_list5 = pickle.load(ff)
sentence_list4.update(sentence_list5)
df= sentence_list4


with open(r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\embedding_list_distilbert.pickle","wb") as fff:
    pickle.dump(sentence_list4, fff, pickle.HIGHEST_PROTOCOL)     
    

         
         
#if os.path.exists(r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\dicttt_of_sentence_embeddings.pickle") == True:
    #print("woohoo")
    #with open(r"D:\Kimlichcova\dictt_of_sentence_embeddings.pickle","wb") as f:
     #   pickle.dump(dictt_of_sentence_embeddings, f, pickle.HIGHEST_PROTOCOL) 
