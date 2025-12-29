# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 12:40:43 2023

@author: yyyyyyyyyyyyyyyyyyyy
"""

from transformers import AutoTokenizer, DistilBertTokenizerFast
import torch
from transformers import DistilBertModel
import re
tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased", truncation_side="left")
finding_start_of_second_sentence=re.compile(r"1")
finding_start_of_first_sentence= re.compile(r"0")
model = DistilBertModel.from_pretrained("distilbert-base-uncased")
text1="Hello, my dog is cute"
text2="meow, i am a cat and yes"

inputs = tokenizer(text1, return_tensors="pt", truncation=True,return_token_type_ids=True)
#model.create_token_type_ids_from_sequences("Hello, my dog is cute")

#dog=DistilBertTokenizerFast.create_token_type_ids_from_sequences(inputs)

print(inputs)
dog=inputs['token_type_ids']
print(dog)
dog= inputs
strwoo=(str((inputs['token_type_ids'])))
tokens_in_current_sentence= re.findall(finding_start_of_first_sentence, string=strwoo)
amount_of_tokens=len(tokens_in_current_sentence) # need to check how many tokens I need to remove here
# I think that two should work here but still need to check
#print(amount_of_tokens)

print(amount_of_tokens)



inputs = tokenizer(text1, return_tensors="pt", truncation=True)
outputs = model(**inputs)

embedding_with_extra_end_token=outputs[0][0]

#print(embedding_with_extra_end_token)


#torch.set_printoptions(profile="full")

embedding_with_extra_end_token=outputs[0][0][-amount_of_tokens:]
print(len(embedding_with_extra_end_token))
good_embeddings= embedding_with_extra_end_token[:-1]
good_embeddings= good_embeddings[1:]
print(len(good_embeddings))




#print(embedding_with_extra_end_token[-1])
#print(good_embeddings[-1])
#print(len(good_embeddings))

#last_hidden_states = outputs.last_hidden_state"""