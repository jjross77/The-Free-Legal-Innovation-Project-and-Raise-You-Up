# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 17:50:38 2023

@author: yyyyyyyyyyyyyyyyyyyy
"""

import numpy as np
import torch
from torch.utils.data import TensorDataset
from torch.utils.data import DataLoader

input = np.random.rand(4, ) # Input data
correct = np.random.rand(4, 1) # Correct answer data

input = torch.FloatTensor(input) # Change to an array that can be handled by pytorch
correct = torch.FloatTensor(correct) # Same as above

print(input)

print(correct)

input is matrix
then a another matrix layer




dataset = TensorDataset(input, correct) # set the data
print(vars(dataset)) # vars prints the contents of the object