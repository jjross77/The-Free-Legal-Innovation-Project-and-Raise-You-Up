# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 06:33:56 2023

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

sen1= "The appellant, Brak, was the main plaintiff in a jury trial for damages arising out of a motor vehicle accident."
sen2= "At the end of trial, after the jury began its deliberations, the defendant, Walsh, brought a motion that no action lay because the plaintiff did not meet the threshold required under s. 267.5(5) of the Insurance Act of suffering a “permanent serious impairment of an important physical, mental or psychological function”." 
dog1=tokenizer(sen1,return_tensors="pt", truncation=True).to("cuda")
dog2=tokenizer(sen2,return_tensors="pt", truncation=True).to("cuda")
print(dog2)
dog4=model(**dog1)
dog3=model(**dog2)
dog3=dog3[0][0][9]
dog4=dog4[0][0][2]
print(dog3)
print(dog4)


sentence_embedding1= torch.mean(dog3, dim=0)# need to test this seems fine
sentence_embedding2= torch.mean(dog4, dim=0)# need to test this seems fine
cos=CosineSimilarity(dim=0, eps=1e-6)
print(cos(sentence_embedding1,sentence_embedding2))


#sentence_embedding1=sentence_embedding1.cpu()
#sentence_embedding2= sentence_embedding2.cpu()
"""
sentence_embedding2=torch.tensor(sentence_embedding2, requires_grad=True)
sentence_embedding1=torch.tensor(sentence_embedding1, requires_grad=True)


sentence_embedding2=sentence_embedding2.numpy() 
sentence_embedding1=sentence_embedding2.numpy() 




                                                                
                                                                      
cos=np.dot(sentence_embedding1,sentence_embedding2)/(norm(sentence_embedding1)*norm(sentence_embedding2))
print(cos)
"""