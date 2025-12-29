# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 16:40:35 2023

@author: yyyyyyyyyyyyyyyyyyyy
"""
from torch.nn import CosineSimilarity
from torch import mean
from pipe_line_to_process_documents2 import document_FIRAC_labeler
import json
import torch
#import torch
docf=document_FIRAC_labeler()
dog=docf.upload_embeddings_from_case_database("embedding_sentences", "%reichman%")
dog2 =docf.upload_embeddings_from_case_database("embedding_sentences", "%T.H. v T.A.%")
doc_1=docf.transform_to_pos_format(dog)
doc_2=docf.transform_to_pos_format(dog2)
#doc_4=[[1],[2]]
doc_1[0]=doc_1[0][715:725]
doc_1[1]=doc_1[1][715:725]
#woo=doc_1[0][0][2]
#woo2=doc_2[0][0][2]
#print(torch.matmul(woo,woo2.T))
print('meow')
# need to find a better way ot save information regarding words being compared

c=docf.cosine_sim_matrix_dot(doc_1,doc_2)
print(c)   
