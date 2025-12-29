# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 10:28:32 2023

@author: yyyyyyyyyyyyyyyyyyyy
"""
import os
import pickle
import numpy as np
embedding_dir_list=os.listdir(r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\embedding_batches_Legal_bert")
path = r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\embedding_batches_Legal_bert"
new_path = r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents"
path_final_dictt_file=new_path + "\\" + "numpy_dict_of_legal_bert_embeddings.pickle"

numpy_dict_of_embeddings = {}
print(embedding_dir_list)
if os.path.exists(r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\numpy_dict_of_legal_bert_embeddings.pickle") == True:
    with open(path_final_dictt_file,"rb") as f1:
        numpy_dict_of_embeddings=pickle.load(f1)
    #load the dictionary from here
    
try:
    for i, embedding_dic in enumerate(embedding_dir_list):
        embeddding_dic_path=path+"\\"+embedding_dic
        
        print(embeddding_dic_path)
        number_iterated_through=str(i)
        embedding_dic_temp=embedding_dic+number_iterated_through
        with open(embeddding_dic_path, "rb") as f2:
            print(embedding_dic_temp)
            embedding_dic_temp=pickle.load(f2)
            print('hello')
        for key, tensor in embedding_dic_temp.items():
            tensor=tensor.cpu()
            numpy_array=tensor.detach().numpy()
            numpy_dict_of_embeddings[key] = numpy_array
           
except Exception as e:
    with open(path_final_dictt_file,"wb") as f3:
        pickle.dump(numpy_dict_of_embeddings, f3, pickle.HIGHEST_PROTOCOL)
    print(e)
    
with open(path_final_dictt_file,"wb") as f4:
    pickle.dump(numpy_dict_of_embeddings, f4, pickle.HIGHEST_PROTOCOL)
numpy_dict_of_embeddings2=  numpy_dict_of_embeddings      
    

                            
        
        
        

        
    
    


