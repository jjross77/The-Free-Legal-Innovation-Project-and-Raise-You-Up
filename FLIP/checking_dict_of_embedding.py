# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 20:33:20 2023

@author: yyyyyyyyyyyyyyyyyyyy
"""
import os
import pickle
with open(r'C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\dicttt_of_sentence_embeddings.pickle', 'rb') as f:
     sentence_list4 = pickle.load(f)
     print(len(sentence_list4))
     for key, values in sentence_list4.items():
         print(f"This sentence is {key}")
        

         
         
if os.path.exists(r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\dicttt_of_sentence_embeddings.pickle") == True:
    print("woohoo")
    #with open(r"D:\Kimlichcova\dictt_of_sentence_embeddings.pickle","wb") as f:
     #   pickle.dump(dictt_of_sentence_embeddings, f, pickle.HIGHEST_PROTOCOL) 
