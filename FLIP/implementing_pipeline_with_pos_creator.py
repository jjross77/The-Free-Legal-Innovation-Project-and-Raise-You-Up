# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 19:46:28 2023

@author: yyyyyyyyyyyyyyyyyyyy
"""
import os
import torch
os.chdir(r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Kimlichcova")
from pipe_line_to_process_documents2 import document_vectorizer

document_vectorizer2=document_vectorizer()

document_name= document_vectorizer2.decide_which_document_to_upload()
text=document_vectorizer2.upload_text()
def processing_pipeline_for_pos(text):
    import torch
    text=document_vectorizer2.pre_process_text(text)
    text=document_vectorizer2.divide_doc_into_sentences(text)
    sentence_list=document_vectorizer2.generate_contexualized_sentences(text)

    for i, sentence in enumerate(sentence_list):
        inputs=document_vectorizer2.tokenize_document(sentence)
        #print(sentence)

        embeddings=document_vectorizer2.generate_embeddings(inputs[0])
        print(len(embeddings[0]))
        del inputs
        torch.cuda.empty_cache() # this seems to be key as well
        # NEED TO IMPLEMENT THESE
        dogoo3=document_vectorizer2.pos_data_creator(sentence[1])
        document_vectorizer2.pos_matcher_and_uploader()
        pos_filtered_embeddings=document_vectorizer2.run_values_thru_pos_model(embeddings[1])
        document_vectorizer2.upload_sentence_to_sentence_embedding_database(i)



        del embeddings
        torch.cuda.empty_cache() # this seems to be key as well
        
      
        
processing_pipeline_for_pos(text) 
previous_case_id= document_vectorizer2.document_id
while True:
    try:
        document_vectorizer3=document_vectorizer()
        text= document_vectorizer3.get_next_document(previous_case_id)
        print(previous_case_id)
        processing_pipeline_for_pos(text)
        previous_case_id=document_vectorizer.document_id
        
        

        
    except Exception as E:
        print(E)
        
