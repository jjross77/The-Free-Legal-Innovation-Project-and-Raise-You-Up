# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 12:17:10 2023

@author: yyyyyyyyyyyyyyyyyyyy
"""
from transformers import DebertaTokenizerFast
from transformers import DataCollatorForTokenClassification

tokenizer = DebertaTokenizerFast.from_pretrained("microsoft/deberta-base", add_prefix_space = True)
from nltk.tokenize import word_tokenize
str1 = "the Bryanses went to the store."
str2 = "he was very happy."
word_divided = word_tokenize(str1)
word_divided2 = word_tokenize(str2)
print(word_divided)
the=tokenizer(word_divided, is_split_into_words=True)
print(the.tokens())
print(the)
print(the.word_ids())
the3 = tokenizer(word_divided2, is_split_into_words=True)
def align_labels_with_tokens(labels, word_ids):
    new_labels = []
    current_word = None
    for word_id in word_ids:
        if word_id != current_word:
            # Start of a new word!
            current_word = word_id
            label = -100 if word_id is None else labels[word_id]
            new_labels.append(label)
        elif word_id is None:
            # Special token
            new_labels.append(-100)
        else:
            # Same word as previous token
            label = labels[word_id]
            # If the label is B-XXX we change it to I-XXX
            if label % 2 == 1:
                label += 1
            new_labels.append(label)

    return new_labels

labels =  [1,2,3,4,2,3,7]
label2 = [1,2,3,4,5]
#word_ids2 = the3.word_ids()
word_ids = the.word_ids()
the2=align_labels_with_tokens(labels, word_ids)
print(the2)
#the4 = align_labels_with_tokens(label2, word_ids2)
#batch = data_collator([tokenized_datasets["train"][i] for i in range(2)])

