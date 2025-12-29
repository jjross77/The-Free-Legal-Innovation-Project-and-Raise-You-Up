# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 18:01:48 2023

@author: yyyyyyyyyyyyyyyyyyyy
"""

import torch
import torch.nn  as nn

#take word embeddings flatten, fill blanks padding
#and forward propagate and then try to reassemble in output

import torch
import torch.nn.functional as F
source = torch.rand(5)
# now we expand to size (7, 11) by appending a row of 0s at pos 0 and pos 6, 
# and a column of 0s at pos 10
# get padding for 
flattened_tensor=source.flatten()

needed_padding= 23040-len(flattened_tensor)
padded_tensor = F.pad(input=source, pad=(0,needed_padding), mode='constant', value=0)
label= 
print(source)
print(result)


class network(nn.Module):
  def __init__(self,input_size, hidden_size,hidden_size2,sentence_size):
      super().__init__()
      self.l1 = nn.Linear(input_size,hidden_size)
      self.l2 = nn.Linear(hidden_size,hidden_size2)
      self.lsentence = nn.Linear(hidden_size2,sentence_size)
      self.l3 = nn.Linear(sentence_size,hidden_size2)
      self.l4 = nn.Linear(hidden_size2,hidden_size)
      self.lfinal = nn.Linear(hidden_size,input_size)
      self.relu = nn.ReLU()




    
  def forward(self,x):
    x = self.l1(x) 
    x = self.relu(x)
    x = self.l2(x)
    x = self.relu(x)
    x = self.lsentence(x)
    x = self.relu(x)
    x = self.l3(x)
    x = self.relu(x)
    x = self.l4(x)
    x = self.relu(x)
    x = self.lfinal(x)

    
    return x
#768x30 flattened is 23040


#model = network().to("cuda") # hiddden layer should be 2 rd the size of the input layer
dog = torch.randn(30,768).to("cuda")
print(model.forward(dog).shape)
print(model)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# create a model from `AE` autoencoder class
# load it to the specified device, either gpu or cpu

# create an optimizer object
# Adam optimizer with learning rate 1e-3
optimizer = optim.Adam(model.parameters(), lr=1e-3)
model = network(23040,10000,2000,768).to("cuda") 

# mean-squared error loss
criterion = nn.MSELoss()


for epoch in range(epochs):
    loss = 0
    for batch_features, _ in train_loader:
        # reshape mini-batch data to [N, 784] matrix
        # load it to the active device
        batch_features = batch_features.view(-1, 784).to(device)
        
        # reset the gradients back to zero
        # PyTorch accumulates gradients on subsequent backward passes
        optimizer.zero_grad()
        
        # compute reconstructions
        outputs = model(batch_features)
        
        # compute training reconstruction loss
        train_loss = criterion(outputs, batch_features)
        
        # compute accumulated gradients
        train_loss.backward()
        
        # perform parameter update based on current gradients
        optimizer.step()
        
        # add the mini-batch training loss to epoch loss
        loss += train_loss.item()
    
    # compute the epoch training loss
    loss = loss / len(train_loader)
    
    # display the epoch training loss
    print("epoch : {}/{}, loss = {:.6f}".format(epoch + 1, epochs, loss))
#layer.bias=nn.Parameter(weight)


#dott=torch.dot(inputt2,inputt)
#print(dott)