# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 13:05:48 2023

@author: yyyyyyyyyyyyyyyyyyyy
"""

import os
import torch
# need to make embedding_sentence not autoupdating and ensure that the ID is always the same
os.chdir(r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Kimlichcova")
from pipe_line_to_process_documents3 import document_vectorizer

document_vectorizer2=document_vectorizer()
#proper_noun_model will be used to  just clean the orginal document when training the model
document_name= document_vectorizer2.decide_which_document_to_upload()
text=document_vectorizer2.upload_text()
#law_list=document_vectorizer2.document_law
#law_list=document_vectorizer2.document_law

document_vectorizer2.init_pos_model()
document_vectorizer2.init_non_sentence_model()

def processing_pipeline_for_pos(text):
    import torch
    text=document_vectorizer2.pre_process_text(text)
    document_vectorizer2.pre_process_law()
    law_label_dic=document_vectorizer2.pre_law_list_creator_0()
    #print(law_label_dic)
    #print(law_label_dic)
    
    
    
    text=document_vectorizer2.divide_doc_into_sentences(text)
    sentence_list=document_vectorizer2.generate_contexualized_sentences(text)

    for i, sentence in enumerate(sentence_list):
        #print(sentence[1])
        inputs=document_vectorizer2.tokenize_document(sentence)

        embeddings=document_vectorizer2.generate_embeddings(inputs[0])
        
        
        pos_sentence=document_vectorizer2.pos_data_creator(sentence[1])
        
        
        found_law=document_vectorizer2.pre_law_data_creator_1(sentence[1])
        
        #print(sentence[1])
        #print(found_law)
        found_law=document_vectorizer2.pre_law_data_creator_2(sentence[1],found_law,law_label_dic)
        #print(found_law)
        
        #print(pos_sentence[1].text)
        law_data=document_vectorizer2.law_data_creator(pos_sentence[1],found_law)
        print(law_data)
        #dogoo3=document_vectorizer2.pos_data_creator(sentence[1])   # this is the most important step need to fix this
        document_vectorizer2.law_matcher_and_uploader(law_data)

        document_vectorizer2.pos_and_pn_matcher_and_uploader()
        unwanted_sentence=document_vectorizer2.run_values_thru_unwanted_sentences(embeddings[1])# seems to be working
        if unwanted_sentence=="true":
            print('this sentence is shit')
            del inputs
            torch.cuda.empty_cache() 
            del embeddings

            continue
 
        
        
        #print(len(embeddings[0]))
        del inputs
        torch.cuda.empty_cache() # this seems to be key as well
        
        # NEED TO IMPLEMENT THESE
        #print(dogoo3[0])
       
        #print(f" meow cats{len(pos_sentence[0][0])}")
        #print(len(dogoo3[0][1]))
        #print(len(dogoo3[0][2]))
        #print(len(dogoo3[0][4]))
        #print(len(dogoo3[0][5]))

        
        pos_filtered_embeddings=document_vectorizer2.run_values_thru_pos_model(embeddings[1])
        #list_of_law=document_vectorizer2.run_values_thru_law_model
        document_vectorizer2.upload_sentence_to_sentence_embedding_database(i)



        del embeddings
        torch.cuda.empty_cache() # this seems to be key as well
        
        
      
        
processing_pipeline_for_pos(text) 
previous_case_id= document_vectorizer2.document_id
while True:
    try:
        document_vectorizer2=document_vectorizer()
        #law_list=document_vectorizer2.document_law
        text= document_vectorizer2.get_next_document(previous_case_id)
        #print(document_vectorizer2.document_law)
        document_vectorizer2.init_pos_model()
        document_vectorizer2.init_non_sentence_model()
        print(previous_case_id)
        processing_pipeline_for_pos(text)
        previous_case_id=document_vectorizer.document_id
        
        

        
    except Exception as E:
        print(E)
        