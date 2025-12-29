# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 21:26:10 2023

@author: yyyyyyyyyyyyyyyyyyyy
"""
from torch import nn

class network(nn.Module):
  def __init__(self,input_size, hidden_size, output_size):
      super().__init__()
      self.l1 = nn.Linear(input_size,hidden_size)
      self.relu = nn.ReLU()
      self.l2 = nn.Linear(hidden_size,output_size)
      self.softmax= nn.Softmax(dim=0)
    
  def forward(self,x):
    x = self.l1(x) 
    x = self.relu(x)
    x = self.l2(x)
    x = self.softmax(x)
    
    return x