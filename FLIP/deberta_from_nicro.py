# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 16:36:12 2023

@author: yyyyyyyyyyyyyyyyyyyy
"""

# To apply DeBERTa into your existing code, you need to make two changes on your code,
# 1. change your model to consume DeBERTa as the encoder
import os
os.chdir(r"C:\Users\yyyyyyyyyyyyyyyyyyyy\AppData\Roaming\Python\Python39\site-packages\DeBERTa\deberta")

from DeBERTa import deberta

import torch

class MyModel(torch.nn.Module):
  def __init__(self):
    super().__init__()
    # Your existing model code
    self.deberta = deberta.DeBERTa(pre_trained='base') # Or 'large' 'base-mnli' 'large-mnli' 'xlarge' 'xlarge-mnli' 'xlarge-v2' 'xxlarge-v2'
    # Your existing model code
    # do inilization as before
    # 
    self.deberta.apply_state() # Apply the pre-trained model of DeBERTa at the end of the constructor
    #
  def forward(self, input_ids):
      print("hello")
    # The inputs to DeBERTa forward are
    # `input_ids`: a torch.LongTensor of shape [batch_size, sequence_length] with the word token indices in the vocabulary
    # `token_type_ids`: an optional torch.LongTensor of shape [batch_size, sequence_length] with the token types indices selected in [0, 1]. 
    #    Type 0 corresponds to a `sentence A` and type 1 corresponds to a `sentence B` token (see BERT paper for more details).
    # `attention_mask`: an optional parameter for input mask or attention mask. 
    #   - If it's an input mask, then it will be torch.LongTensor of shape [batch_size, sequence_length] with indices selected in [0, 1]. 
    #      It's a mask to be used if the input sequence length is smaller than the max input sequence length in the current batch. 
    #      It's the mask that we typically use for attention when a batch has varying length sentences.
    #   - If it's an attention mask then if will be torch.LongTensor of shape [batch_size, sequence_length, sequence_length]. 
    #      In this case, it's a mask indicate which tokens in the sequence should be attended by other tokens in the sequence. 
    # `output_all_encoded_layers`: whether to output results of all encoder layers, default, True
    
    

# 2. Change your tokenizer with the the tokenizer built in DeBERta
from DeBERTa import deberta
vocab_path, vocab_type = deberta.load_vocab(pretrained_id='base')
tokenizer = deberta.tokenizers[vocab_type](vocab_path)
# We apply the same schema of special tokens as BERT, e.g. [CLS], [SEP], [MASK]
max_seq_len = 512
tokens = tokenizer.tokenize('Examples input text of DeBERTa')
print(tokens)
# Truncate long sequence
tokens = tokens[:max_seq_len -2]
# Add special tokens to the `tokens`
tokens = ['[CLS]'] + tokens + ['[SEP]']
print(tokens)
input_ids = tokenizer.convert_tokens_to_ids(tokens)
print(input_ids)
input_mask = [1]*len(input_ids)
print(input_mask)
# padding
paddings = max_seq_len-len(input_ids)

input_ids = input_ids + [0]*paddings
input_mask = input_mask + [0]*paddings

features = {
'input_ids': torch.tensor(input_ids, dtype=torch.int),
'input_mask': torch.tensor(input_mask, dtype=torch.int)
}


deberta_model=MyModel().to("cuda")
config=deberta.config.ModelConfig()
dog=deberta.bert.BertSelfOutput(config)



