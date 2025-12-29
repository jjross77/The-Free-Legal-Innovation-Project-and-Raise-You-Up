# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 23:46:15 2023

@author: yyyyyyyyyyyyyyyyyyyy
"""

import numpy as np
import pandas as pd
import torch
from torch import nn
from torchvision import transforms, datasets, utils
from torch.utils.data import DataLoader, TensorDataset
import json
#from utils.plotting import *
import re
import pickle
import psycopg2
import openpyxl


list_of_labels=[]
list_of_values=[]
wb = openpyxl.load_workbook(r'C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Sparrow_excell3.xlsx')
sheet = wb.active
Column_A = sheet['A'] 
Column_B = sheet['B'] 
Column_C = sheet['C'] 
counterr=0
for sentence, label in zip(Column_A,Column_C):
    if sentence.value =="Sentences":
        continue
    counterr+=1
    if label.value and sentence.value !=None:
        list_of_labels.append(label.value)
        list_of_values.append(sentence.value)
  
    if label.value == None:
        break
    
def processing_pipeline_for_sparrow(sentence_list, label_list):        # need to test this with a sentence later

    import os
    #import torch
    embedding_information_list=[]
    os.chdir(r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Kimlichcova")
    from pipe_line_to_process_documents3 import document_vectorizer
    document_vectorizer2=document_vectorizer()
    sentence_list=document_vectorizer2.generate_contexualized_sentences(sentence_list)
    for sentence,labell in zip(sentence_list,label_list):
        if labell !=8:
            labell=1
        if labell ==8:
            labell=0
        
        sentence[0]=document_vectorizer2.pre_process_text(sentence[0])
        sentence[1]=document_vectorizer2.pre_process_text(sentence[1])
        inputs=document_vectorizer2.tokenize_document(sentence)
        outputs=document_vectorizer2.generate_embeddings(inputs[0])
        document_vectorizer2.non_sentence_matcher_and_uploader(labell)

        document_vectorizer2.reduce_gpu_load(outputs[1])

        #embedding_information_list.append(outputs[0])
        #pos_sentence=document_vectorizer2.pos_data_creator(sentence[1])
        del inputs
        torch.cuda.empty_cache() # this seems to be key as well
       
    
       
    return embedding_information_list
d=processing_pipeline_for_sparrow(list_of_values,list_of_labels)
