# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 18:32:09 2023

@author: yyyyyyyyyyyyyyyyyyyy
"""

import numpy as np
import pandas as pd
import torch
from torch import nn
from torchvision import transforms, datasets, utils
from torch.utils.data import DataLoader, TensorDataset
#from utils.plotting import *

import re
import pickle


counter=0
list_of_labels_2 = []
list_of_values = []
sentence_list = []
with open(r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\numpy_dict_of_legal_bert_embeddings.pickle","rb") as ff:
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
        
list_of_labels_2_train = list_of_labels_2[:8500]
list_of_labels_2_train=np.array(list_of_labels_2_train)

list_of_values_train =  list_of_values[:8500]

targets = torch.Tensor(list_of_labels_2_train)-1
targets=targets.type(torch.LongTensor)
targets=targets.to("cuda")


inputs  = torch.tensor(list_of_values_train)
inputs=inputs.to(torch.float32)
inputs= inputs.to("cuda")
dataset = TensorDataset(inputs, targets)





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

model = network(768, 586, 10).to("cuda") # hiddden layer should be 2 rd the size of the input layer
criterion = nn.CrossEntropyLoss()

optimizer = torch.optim.Adam(model.parameters(), lr=0.001) 



dataloader= DataLoader(dataset, batch_size=50, shuffle=None)
train_loss = []
def trainer(model, criterion, optimizer, dataloader, epochs=180):
    """Simple training wrapper for PyTorch network."""
    
    train_loss = []
    for epoch in range(epochs):  # for each epoch
        losses = 0
        for X, y in dataloader:  # for each batch
            optimizer.zero_grad()       # Zero all the gradients w.r.t. parameters
            y_hat = model(X)  # Forward pass to get output
            #print(y_hat)
            loss = criterion(y_hat, y)  # Calculate loss based on output
            loss.backward()             # Calculate gradients w.r.t. parameters
            optimizer.step()            # Update parameters
            losses += loss.item()       # Add loss for this batch to running total
        train_loss.append(losses / len(dataloader))  # loss = total loss in epoch / number of batches = loss per batch
        print(losses / len(dataloader))
    return train_loss
train_loss=trainer(model, criterion, optimizer, dataloader)

torch.save(model.state_dict(), r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Downloads\model_legal_bert.pth")



#torch.save(model, 'model.pth')

