# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 11:54:27 2023

@author: yyyyyyyyyyyyyyyyyyyy
"""

import numpy as np
import pandas as pd
import torch
from torch import nn
from torchvision import transforms, datasets, utils
from torch.utils.data import DataLoader, TensorDataset
import json
#from utils.plotting import *
# if a word is a blank we need to make sure not to use it when training our pos!!!

import re
import pickle
import psycopg2

conn = psycopg2.connect(dbname="can_law_accessible", user="postgres", password="Meganiscute")
cur = conn.cursor()
cur.execute( f""" SELECT word, embedding, pos_tag
                   FROM pos_labels 
                    ;""")
cur_result= cur.fetchall()
help(json.dump)
list_of_labels_2_train=[]
list_of_values_2_train=[]
for value in cur_result:
    if value[0]:
        if value[2]=="NOUN":
            label=0
            list_of_labels_2_train.append(label)
            value=json.loads(value[1])
            list_of_values_2_train.append(value)
            continue
            
        if value[2]== "VERB":
            label=1
            list_of_labels_2_train.append(label)
            value=json.loads(value[1])
            list_of_values_2_train.append(value)
            continue
        
            
        if value[2]=="OTHER":
            label=2
            list_of_labels_2_train.append(label)
            value=json.loads(value[1])
            list_of_values_2_train.append(value)
            continue
            
        
        
    
   


list_of_labels_2_train=np.array(list_of_labels_2_train)

#list_of_values_train =  list_of_values[:8500]

targets = torch.Tensor(list_of_labels_2_train)
targets=targets.type(torch.LongTensor)
targets=targets.to("cuda")
print(targets)

inputs = torch.tensor(list_of_values_2_train)


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

model = network(768, 586, 3).to("cuda") # hiddden layer should be 2 rd the size of the input layer
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
            print(X)
            print(y)
        
            optimizer.zero_grad()       # Zero all the gradients w.r.t. parameters
            y_hat = model(X)  # Forward pass to get output
            #print(y_hat)
            loss = criterion(y_hat, y)  # Calculate loss based on output
            loss.backward()             # Calculate gradients w.r.t. parameters
            optimizer.step()            # Update parameters
            losses += loss.item()       # Add loss for this batch to running total
        train_loss.append(losses / len(dataloader))  # loss = total loss in epoch / number of batches = loss per batch
        #print(losses / len(dataloader))
    return train_loss
train_loss=trainer(model, criterion, optimizer, dataloader)

#torch.save(model.state_dict(), r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Kimlichcova\model_pos.pth")




#torch.save(model, 'model.pth')

