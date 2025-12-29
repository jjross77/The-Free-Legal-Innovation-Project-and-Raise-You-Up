# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 03:08:50 2023

@author: rossg
"""

def Run_Model(sentence_list, token_list, amount_of_token_list):
    from transformers import  DebertaModel
    import torch
    import subprocess
    import time
    import sys
    import re
    import pickle
    import multiprocessing
    torch.set_printoptions(profile="full")
    torch.cuda.empty_cache()
    device = torch.device("cuda")
    dictt_of_sentence_embeddings= {}
    
    model = DebertaModel.from_pretrained("microsoft/deberta-base").to("cuda")

    try:
        for sentence_3, token, num_token in zip(sentence_list,token_list, amount_of_token_list):
            
            current_sentence = sentence_3
            output = model(**token)
            torch.cuda.empty_cache()
            embedding_with_extra_end_token=output[0][0][-num_token:]
            good_embeddings= embedding_with_extra_end_token[:-1]
            
            sentence_embedding= torch.mean(good_embeddings, dim=0)# need to test this seems fine

            print(sentence_3)
            dictt_of_sentence_embeddings[sentence_3]= sentence_embedding
            


            
            
    except:
        where_we_left_off= current_sentence
        print(where_we_left_off)
        with open(r"D:\Kimlichcova\sentence_embeddings_1.pickle","wb") as f:
            pickle.dump(dictt_of_sentence_embeddings, f, pickle.HIGHEST_PROTOCOL)
        multiprocessing.terminate() 




try:
    for sentence_3, token, num_token in zip(sentence_list,token_list, amount_of_token_list):
        
        current_sentence = sentence_3
        output = model(**token)
        torch.cuda.empty_cache()
        embedding_with_extra_end_token=output[0][0][-num_token:]
        good_embeddings= embedding_with_extra_end_token[:-1]
        
        sentence_embedding= torch.mean(good_embeddings, dim=0)# need to test this seems fine

        print(sentence_3)
        dictt_of_sentence_embeddings[sentence_3]= sentence_embedding
        


        
        
except:
    where_we_left_off= current_sentence
    print(where_we_left_off)
    with open(r"D:\Kimlichcova\sentence_embeddings_1.pickle","wb") as f:
        pickle.dump(dictt_of_sentence_embeddings, f, pickle.HIGHEST_PROTOCOL )
    multiprocessing.terminate() 

    
  