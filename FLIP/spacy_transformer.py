# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 16:24:16 2023

@author: yyyyyyyyyyyyyyyyyyyy
"""
#python -m spacy download en_core_web_trf
import spacy
nlp = spacy.load("en_core_web_trf")
import en_core_web_trf
nlp = en_core_web_trf.load()
doc = nlp("hello world.")

print([ (w.text, w.pos_) for w in doc])
for part_of_speech_parts in doc :

    if part_of_speech_parts.pos_ == "NOUN" or  part_of_speech_parts.pos_ == "PROPN" or part_of_speech_parts.pos_ == "PRON":
        print('hi')
        

    
    if part_of_speech_parts.pos_ == "VERB":
        print('bye')
        
decode mark the word and then 

inputs = tokenizer(existing_sentences, sentence_2, return_tensors="pt", truncation=True, return_token_type_ids=True)
 #print(inputs['token_type_ids'])
 strwoo=(str((inputs['token_type_ids'])))
 tokens_in_current_sentence= re.findall(finding_start_of_second_sentence, string=strwoo)
 amount_of_tokens=len(tokens_in_current_sentence)  # for final token that will be labeled as 
 #print(amount_of_tokens)
 #a 1 still need to remove this or find a way to remove the final token
 # I think I did manage to do this in the end
 inputs = tokenizer(existing_sentences, sentence_2, return_tensors="pt", truncation=True).to("cuda")    
 
 
 
 existing_sentences= existing_sentences + " " + f"{sentence_2}"
    

# save cosine simialrity scores between common nouns and common verbs
