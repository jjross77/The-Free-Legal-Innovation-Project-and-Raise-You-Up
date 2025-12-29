# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 15:09:59 2023

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


def processing_pipeline_for_pos(docs_to_process):
    counterr=0
    for idd in docs_to_process:
        counterr+=1
        if counterr>10:
            document_vectorizer2.__init__()  
            counterr=0
            
            
        text= document_vectorizer2.get_next_document(idd)        
        paragraph_list=document_vectorizer2.divide_doc_into_sections(text)
        paragraph_list=paragraph_list[1:]
        
        if paragraph_list=="too short":
            continue
        if len(paragraph_list) <12:
            continue
        for sentence_number, paragraph in enumerate(paragraph_list):
            paragraph=document_vectorizer2.pre_process_text(paragraph)

            inputs=document_vectorizer2.tokenize_document(paragraph)

            embeddings=document_vectorizer2.generate_embeddings(inputs)
            del inputs
            torch.cuda.empty_cache()
            
            pos_filtered_embeddings=document_vectorizer2.run_values_thru_pos_model(embeddings[1])

            document_vectorizer2.upload_leg_section_to_sentence_database(sentence_number)

            del embeddings
            torch.cuda.empty_cache() # this seems to be key as well
            
            