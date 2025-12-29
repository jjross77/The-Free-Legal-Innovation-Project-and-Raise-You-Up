# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 13:27:28 2023

@author: yyyyyyyyyyyyyyyyyyyy
"""

import torch
import torch.nn as nn
#input_size = 1
#hidden_size=2
#dog =nn.Linear(input_size,hidden_size)
#print(dog)
file_path = r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Downloads\model_project.pth"

import pickle

with open(r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Downloads\input_numpy_for_project.pickle", "rb") as f1:
    inputs_list = pickle.load(f1)

import re
     


inputs  = torch.tensor(inputs_list)
inputs = inputs.to(torch.float32)
#decision_we_want_to_look_at=input()
decision_we_want_to_look_at = 3
print(inputs[decision_we_want_to_look_at])
x = inputs[decision_we_want_to_look_at]


 


#inputs=inputs.to(torch.float32)
#inputs= inputs.to("cuda")




class network(nn.Module):
  def __init__(self,input_size, hidden_size, output_size):
      super().__init__()
      self.l1 = nn.Linear(input_size,hidden_size)
      self.relu = nn.ReLU()
      self.l2 = nn.Linear(hidden_size,output_size)
      self.softmax= nn.Softmax(dim=0)
      
      
      self.weights = {}
      self.biases = {}
      self.inputs = {}
      self.hidden_size = hidden_size
      self.input_size = input_size
      self.output_size = output_size
  def create_weights_and_bias(self, net):
      weight_num = 0
      bias_num = 0
         
      for i, param in enumerate(net.parameters()):
          param = param.clone().detach()
          if (i%2) == 0:
              
              if i>0:
                  weight_num += 1
             
                  self.weights[weight_num] = param
                  continue
              self.weights[weight_num] = param
                            
          if (i%2) != 0:
              if i > 1:
                  bias_num += 1
                  self.biases[bias_num] = param 
                  print(param)
                  continue
              self.biases[bias_num] = param
            

      
  def create_weights(self):
          
      for i , layer in enumerate(self.children()):
          if isinstance(layer, nn.Linear):
              if i >0:
                  i=i-1
              print(i)    
              self.weights[i]=layer.state_dict()['weight']
      return self.weights
  
  def create_bias(self):
      for i , layer in enumerate(self.children()):
          if isinstance(layer, nn.Linear):
              if i >0:
                  i=i-1
              self.biases[i]= layer.state_dict()['bias']
      return self.biases
  
  def import_inputs(self, input_list):
      self.inputs = input_list
      return self.inputs
      
  def forward1(self,x):
      x = self.l1(x) 
      x = self.relu(x)
      
      return x
  
  def forward2(self,x):
      x=self.l2(x)
      x= self.softmax(x)
      return x
  def forward3(self,x):
      x=self.l2(x)
      return x
      

  def forward(self,x):
      x = self.l1(x) 
      x = self.relu(x)
      x=self.l2(x)
      x= self.softmax(x)

      return x
  
  
  def find_percentage_of_layer(self, layer,percentage_dic):
      import copy
      percentage_list = []
      neurons=len(self.weights[layer])
      for neuron in range(neurons):
          print(neuron)
          temp_addition_list=[]
          temp_percentage_list= []   
          
          
          # should be using a dcitonary instead of a list here i think
           
          
          for inputt , w in zip(self.inputs[layer], self.weights[layer][neuron]) :
              temp_addition_list.append(inputt*w) 
          
          next_step=sum(temp_addition_list)+self.biases[layer][neuron]
          print(next_step)
          #print(next_step)
          #if layer == 0:
          #    if next_step<0:
          #        continue
                        
          next_step=next_step*100
          bias_percentage=self.biases[layer][neuron]/next_step
          
          for out in temp_addition_list:
              temp_percentage_list.append(out/next_step)
          temp_percentage_list.append(bias_percentage)
          
          #print(temp_percentage_list)
          percentage_list.append(copy.deepcopy({f"neuron{neuron}":temp_percentage_list}))

          #percentage_dict[layer]= {neuron:temp_percentage_dic[neuron]}
      #print(percentage_list)
      percentage_dic[f"layer{layer}"]=percentage_list
      
      return percentage_dic
  
  #def combine_percentanges_of_a_neuron_in_hidden_layer(self,percentage_dict, layer):
      #for neuron in percentage_dict[layer]:
          
          #extract_specific input value and add to lis 
          #for inputt in neuron:
              #extract s
              #print("hi")
  def find_prediction(self):
      test_for_softmax= net.forward3(self.inputs[1])
      highest_value = torch.tensor([-float("inf")])
      for i, value in enumerate(test_for_softmax):
          if value > highest_value:
              highest_value= value
              neuron_id = i
      prediction_of_model=[neuron_id,highest_value]
              
      return prediction_of_model
      
 
  def find_amount_of_impact_on_final_neuron(self,percentage_dict,prediction_of_model,dictionary_non_sum,dictionarty_sum):
      each_neurons_final_impact_list = []
      predicted_neuron=prediction_of_model[0]
      #print(percentage_dict["layer1"][predicted_neuron][f'neuron{predicted_neuron}'])
      
      for i, amount_of_impact in enumerate(percentage_dict["layer1"][predicted_neuron][f'neuron{predicted_neuron}']):
          #print(amount_of_impact)
          if i+1 == len(percentage_dict["layer1"][predicted_neuron][f'neuron{predicted_neuron}']):
              break
          each_neurons_final_impact_list.append(amount_of_impact)
      
      print(f" final list {each_neurons_final_impact_list}")
      # THIS IS THE MOST IMPORTANT LOOP
      for iiii, impact in enumerate(each_neurons_final_impact_list):
          print(impact)
          iiiii = 0
          print(iiii)

          #print(impact)
          
          
          # ACCESSING THE NEURON
          for  first_layer_neuron in percentage_dict["layer0"][iiii][f"neuron{iiii}"]:                  
               iiiii += 1  
               
                   
                   
                
               these_values=first_layer_neuron/impact*100
              
                   
                   
               if iiiii == len(percentage_dict["layer0"][iiii][f"neuron{iiii}"]):
                   break
               if iiii == 0:
                   dictionarty_sum[iiiii]= these_values
               if iiii != 0:
                   dictionarty_sum[iiiii]+these_values
               print(f"{iiiii}     {first_layer_neuron}") # iiiii corresponds to each input so just need to work with that

               #if iiii > 0:
                   #final_dictionary_string[iiii][f"inputt{iiiii}"] += f"{these_values}"
               #    final_dictionary_sum[f"inputt{iiiii}"] += these_values
               #    continue

               #final_dictionary_string[f"inputt{iiii} {iiiii}"] = f"{these_values}"
               dictionary_non_sum[f"inputt{iiii} {iiiii}"] = these_values
      return dictionary_non_sum
  def graph_for_project_values(dictionarty_sum,first_layer_inputs):
      import pyautogui
      import os
      import time
      print("graphing time!")
      time.sleep(10)
      places_to_click_for_values = [[85,348],[79,402],[78,455],[77,516],[74,570],[74,622],[71,682]]
      places_to_click_for_inputs = [[710,376],[709,424],[706,475],[707,526],[707,573],[705,629],[705,679]]
      for values, place in zip(dictionarty_sum, places_to_click_for_values):
          pyautogui.moveTo(place[0],place[1])
          pyautogui.click()
          pyautogui.typewrite(float(values))
      for inputss, place in zip(first_layer_inputs,places_to_click_for_inputs):
          pyautogui.moveTo(place[0],place[1])
          pyautogui.click()
          pyautogui.typewrite(float(inputss))
    

    
      
      
      
  
               
 
   
          
          
state_dict = torch.load(file_path)
      
net=network(7, 8, 2)
net.load_state_dict(state_dict)

percentage_dic = {}
final_sum_dic = {}
non_sum_dic = {}
net.create_weights_and_bias(net)
#dog = net.create_bias()
#doggy = net.create_weights()

# this consturcing the input
#x = torch.tensor([1.0,1.0,1.0,1.0,1.0,1.0,1.0])
inputs_for_output_layer=net.forward1(x)
inputs_for_output_layer=inputs_for_output_layer.clone().detach()
inputs_layer_list = [x, inputs_for_output_layer]
net.import_inputs(inputs_layer_list)

woowow=net.find_prediction()  
print(f" mewo {woowow}")

dog=net.find_percentage_of_layer(0, percentage_dic) 
dog2 = net.find_percentage_of_layer(1, percentage_dic)
print(percentage_dic)

predicted_neuron=net.find_prediction()

non_sum_dic=net.find_amount_of_impact_on_final_neuron(percentage_dic, predicted_neuron, non_sum_dic, final_sum_dic)
print(non_sum_dic)
print(final_sum_dic)

net.graph_for_project_values(final_sum_dic,x)


#net.find_percentage_of_layer(layer, percentage_dict)
#net.plot
#dog=net.forward2(xzx)
#print(dog)
#xxx=net.forward1(x)
#print(xxx)

woo=net.forward3(inputs_for_output_layer)
#print(woo)
#print(final_dic)

# find the correct final neuron value