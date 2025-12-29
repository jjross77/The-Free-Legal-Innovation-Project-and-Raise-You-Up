# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 17:46:30 2023

@author: yyyyyyyyyyyyyyyyyyyy
"""

#creeating the network
from torch import nn
import numpy as np
import torch

counter=0
list_of_labels_2 = []
list_of_values = []
sentence_list = []
import re
import pickle
with open(r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\numpy_dict_of_embeddings.pickle","rb") as ff:
    original_case_dict=pickle.load(ff)
    
pattern_for_labels= re.compile(r'(\d+): (\d+): (\d+): (.*)') # group 2 is label 2 group 1 is label 1 group 4 is sentence

for key, value in original_case_dict.items():
 
    try:
        keyy=str(key)
        label_regex_obj=pattern_for_labels.search(keyy)
        sentence_group =label_regex_obj.group(4)
        
        label_regex_obj0=label_regex_obj.group(2)
        
        list_of_labels_2.append(label_regex_obj0)
        list_of_values.append(value)
        sentence_list.append(sentence_group)
        
        

    except Exception as e:
        print(e)
len_list_of_labels_2=len(list_of_labels_2)
dataset_in_percentage=len_list_of_labels_2/100
training_amount_of_dataset=dataset_in_percentage*80
training_amount_of_dataset=round(training_amount_of_dataset)


list_of_labels_2_training= list_of_labels_2[:training_amount_of_dataset]
sentence_list_training= sentence_list[:training_amount_of_dataset]
list_of_values_training = list_of_values[:training_amount_of_dataset]

list_of_values_validation = list_of_values[training_amount_of_dataset:]
sentence_list_validation = sentence_list[training_amount_of_dataset:]
list_of_labels_2_validation= list_of_labels_2[training_amount_of_dataset:]
#create dataset
y= np.array(list_of_labels_2_training, dtype='uint8')
x= np.array(list_of_values_training)






class net(nn.Module):
  def __init__(self,input_size,output_size):
      super(net,self).__init__()
      self.l1 = nn.Linear(input_size,5)
      self.relu = nn.ReLU()
      self.l2 = nn.Linear(5,output_size)
      self.softmax= nn.Softmax(dim=1)
    
  def forward(self,x):
    output = self.l1(x) 
    output = self.relu(output)
    output = self.l2(output)
    output = self.softmax(output)
    
    return output

model = net(x.shape[1],1)
criterion = nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(),lr=0.001)
epochs = 1500


#torch.save(model, 'model.pth')