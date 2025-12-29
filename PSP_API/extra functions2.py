# -*- coding: utf-8 -*-
"""
Created on Thu Dec 18 20:57:59 2025

@author: yyyyyyyyyyyyyyyyyyyy
"""

### DONT MESS UP TOP FROM HERE                     
posti=noun_and_verb_chunk_pos_list[+1]

for i3,worddd in enumerate(sentence_word_list):
    
    action_sentence.append(worddd)
    if poss=="AUX" or poss=="VERB":
        words_after_verb=sentence_word_list[i3:]
        action_sentence.insert(words_after_verb,-1)
        
        if wordd in sentence_word_list:
            print("just get the first noun chunk then sub in pos")
            
        # get the proper noun before this
        
        
        
        action_list.append(action_sentence_list)
        action_sentence=[]
        continue
    

    




















print("working on here down up above this line works really well")
action_list=[] 
action_word_list=[]
used_words_list=[]
new_action=""
words_back=0

action_sentence=""
print('# going to break up sentences for actions using pos to create multiple actions')

for i3,noun_verb in  enumerate(noun_and_verb_chunk_list):                        
    print('check for next verb add all beyond first proper nouns')                          
    new_action=""
    possss=noun_and_verb_chunk_pos_list[i3]
    verb_noun_position=position_list[i3]                                                        
    
    sentence_wordd=sentence_word_list[position]
    
    
    if poss=="AUX" or poss=="VERB":
        position=position_list[i3]
        action_word_list=sentence_word_list[position:]
        
        words_back+=1
        wordd_back=noun_and_verb_chunk_list[+1]
        posti=noun_and_verb_chunk_pos_list[+1]
        action_word_list.append(wordd_back)
        
        if posti=="PRON" or posti=="PROPN":
            action_word_list.append(wordd_back)
            action_sentence                                      
        if poss=="AUX" or poss=="VERB":
             break
        #find noun group before this verb
        
            
        # identify verb find closest proper noun or pro noun earlier
        #  use thr saved sentence to add other words if necessary before
        #add everything after
        
        if textt in used_words_list:
            continue
        end_of_last_verb_chunk_position=position                              
       # include nearest chunk to verb
        new_action
        action_list.append(new_action) 
        # go back to noun chunk before
    if last_word_was_a_noun==True:
        print('hi')
        
for actionn in action_list:                                              
    person_comp_info_dic_with_action_copy['action']= str(action_sentence)
    person_comp_info_dic_with_action_copy['transformations'].append(transformations)
    person_comp_info_dic_with_action_copy['action_temporal_placement_in_life_list']=temporal_counter 
    person_comp_info_dic_with_action_copy['noun_and_verb_chunk_list']=noun_and_verb_chunk_list
    person_comp_info_dic_with_action_copy['noun_and_verb_chunk_pos_list']=noun_and_verb_chunk_pos_list
    person_comp_info_dic_with_action_copy['link']=intital_link 
    person_comp_info_dic_with_action_copy['intital_page_text']=website_text                                      
    temporal_counter+=1                       
    #print('starting new sentence add all previous after noun chunk to dictionary')
    person_comp_info_dic_with_action_list.append(person_comp_info_dic_with_action_copy) 
    
 # clear the dictionary
person_comp_info_dic_with_action_copy=copy.deepcopy(person_comp_info_dic_with_action)
print(f"action_sentence {sentence}")
#print(f"transformations {transformations}")
#print(f" noun_chunk {noun_chunk}")
proper_noun_or_pronoun_found=False
verb_found=False 
noun_and_verb_chunk_list=[]
noun_and_verb_chunk_pos_list=[]
used_word_list=[]
position_list=[]
noun_chunk=""
transformations=""
action_sentence=""
keep_sentence1=False
keep_sentence2=False


                      # merge the rest of the sentences
                     # then add the remainder of the sentence
                  #person_comp_info_dic_with_action_copy['object']= noun_chunk 
                  #print(noun_chunk)
                 
                      