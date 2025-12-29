# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 22:42:20 2023

@author: yyyyyyyyyyyyyyyyyyyy
"""
import torch
import torch.nn as nn
import re
import pickle
import numpy as np
from torch.utils.data import DataLoader, TensorDataset



counter=0
list_of_labels_2 = []
list_of_values = []
sentence_list = []

# Model class must be defined somewhere
file_path = r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Downloads\model.pth"
class network(nn.Module):
  def __init__(self,input_size, hidden_size, output_size):
      super().__init__()
      self.l1 = nn.Linear(input_size,hidden_size)
      self.relu = nn.ReLU()
      self.l2 = nn.Linear(hidden_size,output_size)
      self.softmax= nn.Softmax(dim=1)
    
  def forward(self,x):
    x = self.l1(x) 
    x = self.relu(x)
    x = self.l2(x)
    x = self.softmax(x)
    
    return x
state_dict = torch.load(file_path)
model=network(768, 586, 10).to("cuda")


model.load_state_dict(state_dict)
model.eval()

with open(r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\numpy_dict_of_embeddings.pickle","rb") as ff:
    original_case_dict=pickle.load(ff)
    
pattern_for_labels= re.compile(r'(\d+): (\d+): (\d+): (.*)') # group 2 is label 2 group 1 is label 1 group 4 is sentence

for key, value in original_case_dict.items():
 
    try:
        keyy=str(key)
        label_regex_obj=pattern_for_labels.search(keyy)
        sentence_group =label_regex_obj.group(4)
        
        label_2=label_regex_obj.group(2)
        label_2=int(label_2)
        if label_2>10:
            if label_2==22:
                label_2=2
        
        
        list_of_labels_2.append(label_2)
        list_of_values.append(value)
        sentence_list.append(sentence_group)
        
        

    except Exception as e:
        print(e)
        
list_of_labels_2_val = list_of_labels_2[8500:]
#list_of_labels_2_val=np.array(list_of_labels_2_val)
list_of_values_val =  list_of_values[8500:]

#targets = torch.Tensor(list_of_labels_2_val)-1
#print(targets)
#targets=targets.type(torch.LongTensor)
#targets=targets.to("cuda")

inputs  = torch.tensor(list_of_values_val)
inputs=inputs.to(torch.float32)
inputs= inputs.to("cuda")
#dataset = TensorDataset(inputs, targets)
output=model.forward(inputs)

output=output.detach().cpu().numpy()
prediction_list = []

for i, outs in enumerate(output):
    prediction=np.argmax(outs)
    #prediction=int(prediction) +1
    
    prediction_list.append(prediction)
    
list_of_labels_2_val 
count = 0
wrong_list = []
for validation_value, prediciton_value in zip(list_of_labels_2_val, prediction_list):
    validation_value = validation_value-1
    
    if validation_value==prediciton_value:
        count+= +1
        print(count)
    if validation_value!=prediciton_value:
        wrong_list.append(validation_value)
        
        
    
    
    
 
    

with open(r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\prediction_list.pickle", "wb") as f1:
    pickle.dump(prediction_list, f1, pickle.HIGHEST_PROTOCOL)

wrong_list2 = wrong_list
print(wrong_list.count(4))
print(list_of_labels_2_val.count(5))


#output_list.append(output)

#classes = np.argmax(output_list, axis=1)






