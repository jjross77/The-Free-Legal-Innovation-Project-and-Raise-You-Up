# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 15:28:44 2023

@author: yyyyyyyyyyyyyyyyyyyy
"""
import os
os.chdir(r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Kimlichcova")
from pipe_line_to_process_legislation_small_computer import legislation_vectorizer
import torch
import pickle

document_vectorizer2=legislation_vectorizer()
#proper_noun_model will be used to  just clean the orginal document when training the model
#document_vectorizer2.decide_which_document_to_upload()
#text=document_vectorizer2.upload_text()

document_vectorizer2.init_deberta_model()
document_vectorizer2.init_pos_model()
#idd= 4000
idd= 2000
        
text= document_vectorizer2.get_next_document(idd)
paragraph_list=document_vectorizer2.divide_doc_into_sections(text)
#if paragraph_list=="too short":
#    break
#if paragraph_list <5:
#    break
paragraph_list=paragraph_list[1:]
for sentence_number, paragraph in enumerate(paragraph_list):
    
    paragraph=document_vectorizer2.pre_process_text(paragraph)
    print(paragraph)

    inputs=document_vectorizer2.tokenize_document(paragraph)

    embeddings=document_vectorizer2.generate_embeddings(inputs)
    del inputs
    torch.cuda.empty_cache()
    #unwanted_sentence=document_vectorizer2.run_values_thru_unwanted_sentences(embeddings[1])# seems to be working
    #if unwanted_sentence=="true":
    #    print('hi')
        #print(paragraph)
    #    continue
    pos_filtered_embeddings=document_vectorizer2.run_values_thru_pos_model(embeddings[1])

    dog=document_vectorizer2.upload_leg_section_to_sentence_embedding_database(sentence_number)

    del embeddings
    torch.cuda.empty_cache() # this seems to be key as well
#text=document_vectorizer2.pre_process_text(paragraph)
