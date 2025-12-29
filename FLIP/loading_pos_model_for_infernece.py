# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 17:26:30 2023

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
file_path = r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Kimlichcova\model_pos.pth"
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
model=network(768, 586, 3).to("cuda")


model.load_state_dict(state_dict)
print(model.eval())

