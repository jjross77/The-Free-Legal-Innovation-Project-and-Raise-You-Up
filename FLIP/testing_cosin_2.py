# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 02:11:26 2023

@author: yyyyyyyyyyyyyyyyyyyy
"""


from transformers import DistilBertTokenizerFast
from transformers import DistilBertModel
import numpy as np
from numpy.linalg import norm
import torch
from torch.nn import CosineSimilarity
#hi
tokenizer = DistilBertTokenizerFast.from_pretrained("distilbert-base-uncased", truncation_side="left")
model = DistilBertModel.from_pretrained("distilbert-base-uncased").to("cuda")

sen1= "the dog is a great man and I love him he is my friend."
sen2= "the cat is a great man and I love him he is my best friend." 
dog1=tokenizer(sen1,return_tensors="pt", truncation=True).to("cuda")
dog2=tokenizer(sen2,return_tensors="pt", truncation=True).to("cuda")
print(dog2)
dog4=model(**dog1)
dog3=model(**dog2)
dog3=dog3[0][0][6]
dog4=dog4[0][0][6]
print(dog3)
print(dog4)

sentence_embedding1=dog3.cpu()
sentence_embedding2= dog4.cpu()

sentence_embedding2=sentence_embedding2.detach().numpy() 
sentence_embedding1=sentence_embedding1.detach().numpy() 
cos=np.dot(sentence_embedding1,sentence_embedding2)/(norm(sentence_embedding1)*norm(sentence_embedding2))
print(cos)


#sentence_embedding1= torch.mean(dog3, dim=0)# need to test this seems fine
#sentence_embedding2= torch.mean(dog4, dim=0)# need to test this seems fine
#cos=CosineSimilarity(dim=0, eps=1e-6)
#print(cos(sentence_embedding1,sentence_embedding2))