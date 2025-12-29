# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 09:41:10 2023

@author: yyyyyyyyyyyyyyyyyyyy
"""
from transformers import DebertaTokenizerFast

tokenizer = DebertaTokenizerFast.from_pretrained("microsoft/deberta-base", truncation_side="left")
sentences = ["hello my name is marvin i d d d d d d d d d d d d d d  d d d d d d d d d dd  d d dd  dd  ","adding this to the other one"]
iterator_number = 0
existing_sentences = ""
for i, sentence in enumerate(sentences):
    iterator_number +=1
    iterator_minus_one = iterator_number-1
    if i==0:
        existing_sentences= f"{sentence}"
    else:
        existing_sentences= existing_sentences + " " f"{sentence}"
    print(existing_sentences)
    if existing_sentences number_of_spaces >:
        
    inputs = tokenizer(sentence, return_tensors="pt").to("cuda")   
    
print(inputs[0])


#truncaiton_side is the value 
#save the input from earlier add that to the next string input tokenize it, if the tokenized output is longer than the model is able
#to take then remove tokens from the front until it meets the required length, 