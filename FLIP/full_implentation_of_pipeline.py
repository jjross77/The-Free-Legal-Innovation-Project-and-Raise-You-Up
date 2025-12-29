# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 22:31:25 2023

@author: yyyyyyyyyyyyyyyyyyyy
"""
import os
import torch
os.chdir(r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Kimlichcova")
from pipe_line_to_process_documents2 import document_vectorizer

document_vectorizer=document_vectorizer()

document_name= document_vectorizer.decide_which_document_to_upload()
text=document_vectorizer.upload_text(document_name)
def processing_pipeline_for_pos(text):
    import torch
    text=document_vectorizer.pre_process_text(text)
    text=document_vectorizer.divide_doc_into_sentences(text)
    sentence_list=document_vectorizer.generate_contexualized_sentences(text)

    for sentence in sentence_list:
        inputs=document_vectorizer.tokenize_document(sentence)
        
        embeddings=document_vectorizer.generate_embeddings(inputs[0])
        
        dogoo3=document_vectorizer.pos_data_creator(sentence[1])
        document_vectorizer.pos_matcher_and_uploader()
        del embeddings
        del inputs # thsi is hte key to freeing up memeory wow
        torch.cuda.empty_cache() # this seems to be key as well

processing_pipeline_for_pos(text) 
previous_case_id= document_vectorizer.document_id
while True:
    try:
        document_vectorizer=document_vectorizer()
        text= document_vectorizer.get_next_document(previous_case_id)
        print(previous_case_id)
        processing_pipeline_for_pos(text)
        previous_case_id=document_vectorizer.document_id
        
        

        
    except Exception as E:
        print(E)
        
        
